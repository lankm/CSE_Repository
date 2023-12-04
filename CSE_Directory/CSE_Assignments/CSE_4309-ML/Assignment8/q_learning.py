import numpy as np
from random import random, shuffle

class Action:
    arrows = ['^','<','v','>']
    names = ['up','left','down','right']
    translate = [(1,0),(0,-1),(-1,0),(0,1)]

    def __init__(self, direction: str):
        direction = direction.lower()
        if direction not in Action.names:
            raise ValueError('Invalid action')
        
        self.direction = Action.names.index(direction)

    def ApplyTo(self, state):
        translation = Action.translate[self.direction]
        Ty = translation[0]
        Tx = translation[1]
        return (state[0]+Ty, state[1]+Tx)
    
    def RotateLeft(self):
        return Action(Action.names[(self.direction+1)%4])
    def RotateRight(self):
        return Action(Action.names[(self.direction-1)%4])

    def Actions():
        return [Action(name) for name in Action.names]

    def __eq__(self, other):
        if other == None:
            return False
        return self.direction == other.direction
    def __hash__(self):
        return hash(self.direction)
    def __str__(self):
        return Action.arrows[self.direction]
    def __repr__(self):
        return Action.arrows[self.direction]

class Environment:
    def __init__(self, data_file, ntr):
        obstacles = []
        terminals = {}

        with open(data_file, 'r') as filestream:
            rows = filestream.readlines()
            num_rows = len(rows)
            num_cols = len(rows[0].split(','))

            for y, row in enumerate(rows):
                for x, val in enumerate(row.split(',')):
                    pos = (num_rows-y, x+1)
                    val = val.strip()

                    if val == 'X':      # obstacle
                        obstacles.append(pos)
                    elif val == 'I':    # start
                        start_state = pos
                    elif val != '.':    # terminal
                        terminals[pos] = float(val)
        
        self.obstacles = obstacles # list
        self.terminals = terminals # dictionary
        self.start_state = start_state # tuple
        self.num_rows = num_rows # int
        self.num_cols = num_cols # int
        self.ntr = ntr # float
    
    def reward(self, state):
        if state in self.obstacles:
            raise ValueError('Can not be inside an obstacle')
        elif state in self.terminals:
            return self.terminals[state]
        else:
            return self.ntr
    def ExecuteAction(self, state, action: Action):
        rand = random()
        if rand < .1:
            action = action.RotateLeft()
        elif rand > .9:
            action = action.RotateRight()
        
        (y, x) = action.ApplyTo(state)
        if (y, x) in self.obstacles: # if hitting obstacle
            return state
        elif (y <= 0 or y > self.num_rows) or (x <= 0 or x > self.num_cols): # if hitting side of map
            return state
        return (y, x)

    def __str__(self):
        return f'start_state = {self.start_state}\nterminals = {self.terminals}\nstart_state = {self.start_state}\nnum_rows = {self.num_rows}\nnum_cols = {self.num_cols}'

class Actor:
    totalActionsExecuted = 0
    def __init__(self, env: Environment):
        self.env = env
        self.cur_location = env.start_state
    
    def SenseStateAndReward(self):
        return self.cur_location, self.env.reward(self.cur_location)
    def ExecuteAction(self, action: Action):
        self.cur_location = self.env.ExecuteAction(self.cur_location, action)
        Actor.totalActionsExecuted += 1
    
    def __str__(self):
        return f'{self.cur_location}'

# =============================================================================
def Utility(Q, state):
    return max([ 
        Q.get((state,action), 0) for action in Action.Actions()+[None] 
    ])
def BestAction(Q, state):
    return Action(Action.names[
        np.argmax([ Q.get((state,action), 0) for action in Action.Actions()])
    ])
def NextAction(Q, N, Ne, state):
    f_vals = {}
    for action in Action.Actions():
        f_vals[action] = f(Q.get((state,action), 0),N.get((state,action), 0), Ne)
    
    max_v = max(f_vals.values())
    for key in list(f_vals.keys()):
        if f_vals[key] != max_v:
            del f_vals[key]

    ties = list(f_vals.keys())
    shuffle(ties)
    return ties[0]

def Q_Learning_Update(s_p, r_p, s, r, a, Q, N, gamma, env: Environment):
    if s_p in env.terminals:
        Q[(s_p, None)] = r_p
    if s != None:
        N[(s,a)] = N.get((s,a), 0) + 1
        c = 20/(19+N[(s,a)])

        prev_Q = (1-c)*Q.get((s,a), 0)
        new_Q =    (c)*(r + gamma*Utility(Q, s_p))
        Q[(s,a)] = prev_Q + new_Q

def f(u, n, ne):
    if n < ne:
        return 1
    else:
        return u

def output(Q, env: Environment):
    utilities = np.zeros((env.num_rows, env.num_cols))
    policy = np.empty((env.num_rows, env.num_cols),dtype=str)

    for i in range(env.num_rows):
        for j in range(env.num_cols):
            state = (i+1,j+1)

            utility = Utility(Q, state)
            best_action = BestAction(Q, state)

            if state in env.terminals: # if terminal. can also be extracted from Q but harder to read the code
                policy[i,j] = 'o'
                utilities[i,j] = env.terminals[state]
            elif state in env.obstacles:  # if obstacle. can also be extracted from Q but harder to read the code
                policy[i,j] = 'x'
                utilities[i,j] = 0
            else:
                policy[i,j] = best_action.__str__()
                utilities[i,j] = utility


    # print utilities for each state
    print('utilities:')
    for row in np.flip(utilities, axis=0):
        for val in row:
            print('%6.3f ' % val,end='')
        print()
    print()
    # print the policy for each state
    print('policy:')
    for row in np.flip(policy, axis=0):
        for val in row:
            print('%6s ' % val,end='')
        print()

def AgentModel_Q_Learning(environment_file, ntr, gamma, number_of_moves, Ne):
    # coordinates are (y, x) starting at 1 as defined in the slides
    env = Environment(environment_file, ntr)

    Q = {} # Q values for (s,a)
    N = {} # # of occurences of (s,a)
    while Actor.totalActionsExecuted < number_of_moves:
        s = None # previous state
        r = None # previous reward
        a = None # next action
        actor = Actor(env) # actor starts at start state of env
        while Actor.totalActionsExecuted < number_of_moves:
            s_p, r_p = actor.SenseStateAndReward()
            Q_Learning_Update(s_p, r_p, s, r, a, Q, N, gamma, env)
            if s_p in env.terminals: break
            a = NextAction(Q, N, Ne, s_p)
            actor.ExecuteAction(a)
            s, r = s_p, r_p

    output(Q, env)
    