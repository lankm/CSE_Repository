import numpy as np
import skvideo
from KalmanFilter import KalmanFilter

from skimage import morphology
from skimage.color import rgb2gray
from skimage.measure import label, regionprops

# track each object as a kalman filter
class MotionDetector:
    def __init__(self, frames, frame_hysteresis, motion_threshold, distance_threshold, frames_to_skip, max_objects,  blob_size=4):
        self.frame_hysteresis = frame_hysteresis # delay between activation/deactivation (frame distance)
        self.motion_threshold = motion_threshold # filter raw noise. (0-255)
        self.distance_threshold = distance_threshold # threshold for matching objects and tracked objects (pixel distance)
        self.frames_to_skip = frames_to_skip # doesn't have to be every frame (frame distance)
        self.max_objects = max_objects # self explainatory
        if max_objects < 0:
            self.max_objects = float('inf')
        self.blob_size = blob_size # dialation size when detecting

        self.frames = frames # just a reference to video data so frame data doesn't have to be passed. instead frame number can be passed

        self.end = 2 - self.frames_to_skip # done so first update initializes
        self.objects = [] # contains active and inactive KalmanFilters
        # initialization not required due to qtvideo calling first update. update is the same as initialization
    
    # returns bounding boxes and centroids of objects
    def detect(self, frame):
        # load required frames
        t0 = rgb2gray(self.frames[frame])*255
        t1 = rgb2gray(self.frames[frame-1])*255
        t2 = rgb2gray(self.frames[frame-2])*255

        # calculate differences between frames and get min
        d1 = abs(t0-t1).astype(np.uint8)
        d2 = abs(t1-t2).astype(np.uint8)
        d = np.minimum(d1,d2)

        # make into boolean image
        mask = d >= self.motion_threshold
        d[mask] = 255
        d[~mask] = 0

        # dilate each pixel with a circular window
        selem = morphology.disk(self.blob_size)
        d = morphology.dilation(d, selem)

        # detect objects and extract relevent information
        labels = label(d)
        regions = regionprops(labels)
        boxes = []
        centroids = []
        for region in regions:
            y1, x1, y2, x2 = region.bbox
            boxes.append((x1,y1,x2-x1,y2-y1))
            y0, x0 = region.centroid
            centroids.append((x0,y0))

        return np.array(boxes), np.array(centroids)

    # updates up to a given frame by iterating
    def update_to(self, frame):
        if frame < self.end:
            self.objects = []
            self.end = frame
        
        while(self.end + self.frames_to_skip <= frame):
            self.update_single(self.end)
            self.end += self.frames_to_skip

    # a simple update that only considers the last known frame
    def update_single(self, frame):
        # reinitialize if previous frame
        if frame < self.end:
            self.objects = []
        self.end = frame

        # removing tracked objects that have not been detected recently
        objects = []
        for object in self.objects:
            if frame-object.end < self.frame_hysteresis:
                objects.append(object)
        self.objects = objects

        # updating based on detection
        boxes, centroids = self.detect(frame)
        for centroid in centroids:

            matched = False
            # if match is found
            for object in self.objects:
                prediction, _ = object.predict(frame)
                if np.linalg.norm(prediction-centroid) < self.distance_threshold:
                    matched = True
                    object.update(centroid, frame)
                    break
            
            # if a match is not found
            if not matched:
                # make a new inactive kalman filter if enough space
                if len(self.objects) < self.max_objects:
                    self.objects.append(KalmanFilter(centroid, frame, False))
        
        # activating objects which have been dectected for a while
        for object in self.objects:
            if object.age() >= self.frame_hysteresis:
                object.active = True
