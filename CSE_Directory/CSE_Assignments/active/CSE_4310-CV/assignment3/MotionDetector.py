import numpy
import skvideo
from KalmanFilter import KalmanFilter

# track each object as a kalman filter
class MotionDetector:
    def __init__(self):
        self.frame_hysteresis = None # delay between activation/deactivation
        self.motion_threshold = None # filter raw noise
        self.distance_threshold = None # threshold for matching candidates and tracked objects
        self.frames_to_skip = None # doesn't have to be ever frame
        self.max_objects = None # 

# =============================================================================

def main():
    pass

if __name__ == '__main__':
    main()
