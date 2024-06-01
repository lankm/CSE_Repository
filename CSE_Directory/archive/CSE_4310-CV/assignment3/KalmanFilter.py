import numpy as np

# keeps track of one object
class KalmanFilter:
    def __init__(self, pos, start, active):
        self.pos = np.array(pos)
        self.vel = np.array([0,0]) # initially no velocity information is known
        self.acc = np.array([0,0])
        self.active = active       # generally initiallizes to false

        self.start = start # constant
        self.end = start   # changes with update

        self.history = {}
        self.history[start] = pos
    
    def predict(self, frame):
        dt = frame - self.end
        v = self.vel + dt*self.acc
        p = self.pos + dt*self.vel + .5*dt**2*self.acc
        return p, v

    # update given a new position. alpha is the similar to the 'control matrix'
    def update(self, new_pos, frame, alpha=0.5):
        if frame in self.history: # should already be handled by calling class
            return
        
        # calculate new values given new position. assume constant acceleration between a to b
        dt = frame - self.end
        p, v = self.predict(frame) # previously expected state
        new_vel = (new_pos - self.pos)/dt # assuming new_pos is correct, actual velocity
        new_acc = 0 # 2*(new_vel - self.vel)/dt # assuming new_vel is correct, actual acceleration

        # update state. alpha factor implemented due to merging objects causing fast acceleration
        self.pos = (1-alpha)*p        + (alpha)*new_pos
        self.vel = (1-alpha)*v        + (alpha)*new_vel
        self.acc = (1-alpha)*self.acc + (alpha)*new_acc

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