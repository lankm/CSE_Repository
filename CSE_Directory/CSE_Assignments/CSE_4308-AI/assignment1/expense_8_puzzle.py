# the relationship between a state and an action can probably be coded better.

import sys
import copy

class Action:
  def __init__(self, num: int, action: str):
    self.num = num

    match action.lower():
      case 'up':
        self.action = 'Up'
      case 'right':
        self.action = 'Right'
      case 'down':
        self.action = 'Down'
      case 'left':
        self.action = 'Left'
      case _:
        self.action = 'ERROR'
  
  def new_pos(self, pos: (int, int)) -> (int, int):
    match self.action.lower():
      case 'up':
        return (pos[0]-1,pos[1])
      case 'right':
        return (pos[0],pos[1]+1)
      case 'down':
        return (pos[0]+1,pos[1])
      case 'left':
        return (pos[0],pos[1]-1)
      case _:
        return 'ERROR'

  def __str__(self):
    return f'Move {self.num} {self.action}'

class State:
  def __init__(self, data: list[list[int]]):
    self.data = data
  def from_file(filename: str):
    file = open(filename)

    state = []
    for row in file.readlines()[:-1]:
      state.append(list(map(int, row.split())))

    return State(state)
  
  def find_num(self, val) -> (int, int):
    for (i, row) in enumerate(self.data):
      for (j, num) in enumerate(row):
        if num == val:
          return (i, j)
        
    return (-1,-1)
  def valid_actions(self) -> list[Action]:
    idx_zero = self.find_num(0)
    data = self.data

    # this is hardcoded. TODO: fix it
    match idx_zero:
      case (0,0):
        return [Action(data[1][0],'up'),
                Action(data[0][1],'left')]
      case (0,1):
        return [Action(data[0][0],'right'),
                Action(data[0][2],'left'),
                Action(data[1][1],'up')]
      case (0,2):
        return [Action(data[0][1],'right'),
                Action(data[1][2],'up')]
      case (1,0):
        return [Action(data[0][0],'down'),
                Action(data[2][0],'up'),
                Action(data[1][1],'left')]
      case (1,1):
        return [Action(data[0][1],'down'),
                Action(data[1][2],'left'),
                Action(data[1][0],'right'),
                Action(data[2][1],'up')]
      case (1,2):
        return [Action(data[0][2],'down'),
                Action(data[1][1],'right'),
                Action(data[2][2],'up')]
      case (2,0):
        return [Action(data[1][0],'down'),
                Action(data[2][1],'left')]
      case (2,1):
        return [Action(data[2][0],'right'),
                Action(data[1][1],'down'),
                Action(data[2][2],'left')]
      case (2,2):
        return [Action(data[2][1],'right'),
                Action(data[1][2],'down')]
  def apply_action(self, action: Action):
    data = copy.deepcopy(self.data)

    pos1 = self.find_num(action.num)
    pos2 = action.new_pos(pos1)

    temp = data[pos1[0]][pos1[1]]
    data[pos1[0]][pos1[1]] = data[pos2[0]][pos2[1]]
    data[pos2[0]][pos2[1]] = temp

    return State(data)
  def goal_test(self, state) -> bool:
    for (i, row) in enumerate(state.data):
      for (j, num) in enumerate(row):
        if num != self.data[i][j]:
          return False
    return True

  def __str__(self):
    output = ""
    for row in self.data:
      output += '['

      for num in row[:-1]:
        output += f'{num}, '

      output += f'{row[-1]}]\n'

    return output

class Node:
  def __init__(self, state: State, cost: float, parent, action: Action):
    self.state = state
    self.parent = parent
    self.action = action
    self.cost = cost
  
  def generate_childeren(self) -> list:
    childeren = []

    for action in self.state.valid_actions():
      childeren.append(Node(
        self.state.apply_action(action),
        self.cost + 1.0,
        self,
        action))
    return childeren
  
  def __str__(self):
    output = ''

    if self.parent is not None:
      output += f'{self.parent}'
    
    output += f'{self.action} - {self.cost}\n{self.state}'

    return output

def bfs_search(start_state: State, goal_state: State, dump_flag: bool):
  fringe = [Node(start_state, 0.0, None, None)]
  visited = []

  print(fringe[0].generate_childeren()[0])
    
  return 0
def ucs_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0
def dfs_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0
def dls_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0
def ids_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0
def greedy_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0
def a_search(start_state, goal_state, dump_flag):
  if dump_flag:
    print(dump_flag)
    
  return 0

def main():
  argc = len(sys.argv)

  if argc < 3:
    print('Expected:\nexpense_8_puzzle.py <start-file> <goal-file> <method?> <dump-flag?>')
    return 1

  start_file = sys.argv[1]
  goal_file = sys.argv[2]

  method = "a*"
  dump_flag = "false"
  if argc > 3:
    arg3 = sys.argv[3]

    if arg3 == "true" or arg3 == "false": # if arg3 is dump_flag
      dump_flag = arg3
    else:                                 #if arg3 is method
      method = arg3

      if argc > 4:
        dump_flag = sys.argv[4]

  # dump flag matching
  match dump_flag.lower():  
    case "true":
      dump_flag = True
    case "false":
      dump_flag = False
    case _:
      print('Invalid dump flag. Choose from:\ntrue, or false')
      return 1
  
  # file io
  start_state = State.from_file(start_file)
  goal_state = State.from_file(goal_file)

  # method matching
  match method.lower():
    case "bfs":
      bfs_search(start_state, goal_state, dump_flag)
    case "ucs":
      ucs_search(start_state, goal_state, dump_flag)
    case "dfs": # optional
      dfs_search(start_state, goal_state, dump_flag)
    case "dls": # optional
      dls_search(start_state, goal_state, dump_flag)
    case "ids": # optional
      ids_search(start_state, goal_state, dump_flag)
    case "greedy":
      greedy_search(start_state, goal_state, dump_flag)
    case "a*":
      a_search(start_state, goal_state, dump_flag)
    case _:
      print('Invalid method type. Choose from:\nbfs, ucs, dfs, dls, ids, greedy, or a*')
      return 1
    
  return 0

if __name__ == "__main__":
  main()