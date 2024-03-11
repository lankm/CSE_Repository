import numpy as np

# keeps track of one object
class KalmanFilter:
    def __init__(self, pos, start, active):
        self.pos = np.array(pos)
        self.vel = np.array([0,0])
        self.active = active

        self.start = start # constant
        self.end = start   # changes with update

        self.history = {}
        self.history[start] = pos
    
    def predict(self, frame):
        dt = frame - self.end
        return self.pos + dt*self.vel

    def update(self, pos, frame):
        dt = frame - self.end
        self.vel = (pos-self.pos)/dt

        self.end = frame

    def age(self):
        return self.end - self.start
    
    def __str__(self):
        return f'pos: {self.pos}, active: {self.active}, end: {self.end}'
        

# =============================================================================
    
def main():
    pass

if __name__ == '__main__':
    main()