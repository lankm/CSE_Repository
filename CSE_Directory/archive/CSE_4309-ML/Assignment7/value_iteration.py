import numpy as np

def read_file(data_file):
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
        if val == 'X':
          obstacles.append(pos)
        elif val != '.':
          terminals[pos] = float(val)
        

  return obstacles, terminals, num_rows, num_cols

arrows = ['^','<','v','>'] # up, left, down, right
avail_actions = {0: (1,0), 1:(0,-1), 2:(-1,0), 3:(0,1)} # up, left, down, right
# retrieves the next states and their probabilities given a state and a non-deterministic action
def possible_results(obstacles, state, action, num_rows, num_cols):
  states = {}
  probs = [.1,.8,.1]
  for i, act in enumerate(range(action-1,action+2)):
    new_state = next_state(obstacles, state, act, num_rows, num_cols)
    if new_state in states.keys():
      states[new_state] += probs[i]
    else:
      states[new_state] = probs[i]
  
  return states
# retrieves the next state given a start state, and deterministic action.
def next_state(obstacles, state, action, num_rows, num_cols):
  dy, dx = avail_actions[action%4]
  y, x = state
  new_state = y+dy, x+dx
  ny, nx = new_state

  if new_state in obstacles: # if hitting obstacle
    return state
  elif (ny<=0 or ny>num_rows) or (nx<=0 or nx>num_cols): # if out of bounds
    return state
  else:
    return new_state

def reward(state,   terminals, ntr):
  if state not in terminals.keys():
    return ntr
  else:
    return terminals[state]

def value_iteration(data_file, ntr, gamma, K):
  # setup
  obstacles, terminals, num_rows, num_cols = read_file(data_file) # world = (obstacles, terminals)
  states = [(y+1, x+1) for x in range(num_cols) for y in range(num_rows) # all possible states
            if (y+1, x+1) not in obstacles and (y+1, x+1) not in terminals] # exclude obstacles and terminals for performance
  
  # initialization
  utilities = np.zeros((num_rows, num_cols))
  policy = np.empty((num_rows, num_cols),dtype=str)
  for obstacle in obstacles:
    y, x = obstacle
    utilities[y-1][x-1] = 0
    policy[y-1][x-1] = 'x'
  for terminal in terminals:
    y, x = terminal
    utilities[y-1][x-1] = terminals[terminal]
    policy[y-1][x-1] = 'o'
  
  # main loop
  for _ in range(K):
    utilities_copy = np.copy(utilities)

    for state in states:
      y, x = state

      # list for each action's results
      results = [(possible_results(obstacles, state, action, num_rows, num_cols),action) for action in avail_actions] # list of dictionaries of state->prob
      
      # calculating the sums of utilities for each possible action
      action_utilities = []
      for dict in results:
        action_utility = 0
        for possible_state in dict[0].keys():
          ny, nx = possible_state
          action_utility += dict[0][possible_state] * utilities_copy[ny-1][nx-1]
        action_utilities.append(action_utility)

      # policy and utility calculation
      policy[y-1][x-1] = arrows[list(avail_actions.keys())[action_utilities.index(max(action_utilities))]]
      utilities[y-1][x-1] = reward(state, terminals, ntr) + gamma*max(action_utilities)

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
      print('%6.3s ' % val,end='')
    print()
