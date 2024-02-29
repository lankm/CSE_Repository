import numpy
import skvideo
from KalmanFilter import KalmanFilter

# track each object as a kalman filter
class MotionDetector:
    def __init__(self):
        self.frame_hysteresis = None
        self.motion_threshold = None
        self.distance_threshold = None
        self.frames_to_skip = None
        self.max_objects = None

# =============================================================================

def main():
    pass

if __name__ == '__main__':
    main()
