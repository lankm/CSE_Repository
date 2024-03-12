import numpy as np

# keeps track of one object
class KalmanFilter:
    def __init__(self, pos, start, active):
        self.pos = np.array(pos)
        self.vel = np.array([0,0]) # initially no velocity information is known
        self.active = active       # generally initiallizes to false

        self.start = start # constant
        self.end = start   # changes with update

        self.history = {}
        self.history[start] = pos
    
    def predict(self, frame):
        dt = frame - self.end
        return self.pos + dt*self.vel

    # update given a new position. alpha is the similar to the 'control matrix'
    def update(self, new_pos, frame, alpha=0.5):
        if frame in self.history: # should already be handled by calling class
            return

        # update velocity
        dt = frame - self.end
        new_vel = (new_pos-self.pos)/dt
        self.vel = (1-alpha)*self.vel + (alpha)*new_vel
        # update position
        self.pos = (1-alpha)*self.pos + (alpha)*new_pos

        # update history and end
        self.history[frame] = new_pos
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