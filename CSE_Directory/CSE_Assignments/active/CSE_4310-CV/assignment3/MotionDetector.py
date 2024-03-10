import numpy as np
import skvideo
from KalmanFilter import KalmanFilter

from skimage import morphology
from skimage.color import rgb2gray
from skimage.measure import label, regionprops

# track each object as a kalman filter
class MotionDetector:
    def __init__(self, frame_hysteresis, motion_threshold, distance_threshold, frames_to_skip, max_objects, frames):
        self.frame_hysteresis = frame_hysteresis # delay between activation/deactivation
        self.motion_threshold = motion_threshold # filter raw noise. (0-255)
        self.distance_threshold = distance_threshold # threshold for matching candidates and tracked objects
        self.frames_to_skip = frames_to_skip # doesn't have to be ever frame
        self.max_objects = max_objects # 

        self.gray_frames = np.array([rgb2gray(frame)*255 for frame in frames])

        # TODO init with first 3 frames
    
    def detect(self, frame):
        # load required frames
        t0 = self.gray_frames[frame]
        t1 = self.gray_frames[frame-1]
        t2 = self.gray_frames[frame-2]

        # calculate differences between frames and get min
        d1 = abs(t0-t1).astype(np.uint8)
        d2 = abs(t1-t2).astype(np.uint8)
        d = np.minimum(d1,d2)

        # make into boolean image
        mask = d >= self.motion_threshold
        d[mask] = 255
        d[~mask] = 0

        # dilate each pixel with a circular window
        selem = morphology.disk(9)
        d = morphology.dilation(d, selem)

        # detect candidates
        labels = label(d)
        regions = regionprops(labels)
        boxes = []
        for region in regions:
            y1, x1, y2, x2 = region.bbox
            boxes.append((x1,y1,x2-x1,y2-y1))

        return boxes

# =============================================================================

def main():
    pass

if __name__ == '__main__':
    main()
