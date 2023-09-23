import sys
import copy

class Stats:
  def __init__(self):
    self.nodes_popped = 0
    self.nodes_expanded = 0
    self.nodes_generated = 0
    self.max_fringe_size = 0
  
  def popped_node(self):
    self.nodes_popped += 1
  def expanded_node(self):
    self.nodes_expanded += 1
  def generated_nodes(self, num):
    self.nodes_generated += num
  def update_max_fringe_size(self, fringe_size):
    self.max_fringe_size = max(self.max_fringe_size, fringe_size)

class Logger:
  def __init__(self, active, filename):
    self.active = active
    if active:
      self.file = open(filename, 'wt')
  
  def log_args(self, args):
    if not self.active:
      return 0
    
    self.file.write(f'Command-Line Arguments : {args}\n')

    return 0
  def log_method(self, method):
    if not self.active:
      return 0
    
    self.file.write(f'Method Selected: {method}\n')
    self.file.write(f'Running {method}\n')

    return 0
  def log_successors(self, cur_node, num_of_childeren):
    if not self.active:
      return 0
    
    self.file.write(f'Generating successors to {cur_node}\n')
    self.file.write(f'        {num_of_childeren} successors generated\n')

    return 0
  def log_closed(self, closed):
    if not self.active:
      return 0

    self.file.write(f'        Closed: {closed}\n')

    return 0
  def log_fringe(self, fringe):
    if not self.active:
      return 0
    
    self.file.write(f'        Fringe: [\n')

    for node in fringe:
      self.file.write(f'                {node}\n')
    self.file.write(f'                ]\n')

    return 0
  def log_success(self, cur_node, stats: Stats):
    if not self.active:
      return 0
    
    self.file.write(f'Goal Found: {cur_node}\n')
    self.file.write(f'        Nodes Popped: {stats.nodes_popped}\n')
    self.file.write(f'        Nodes Expanded: {stats.nodes_expanded}\n')
    self.file.write(f'        Nodes Generated: {stats.nodes_generated}\n')
    self.file.write(f'        Max Fringe Size: {stats.max_fringe_size}\n')

    return 0

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

  def __str__(self) -> str:
    return f'Move {self.num} {self.action}'

class State:
  def __init__(self, data: list[list[int]]):
    self.data = data
  def from_file(filename: str):
    file = open(filename, 'rt')

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
  def heuristic(self, goal_state):
    total = 0
    for i in range(9):
      loc1 = self.find_num(i)
      loc2 = goal_state.find_num(i)
      dx = abs(loc1[0]-loc2[0])
      dy = abs(loc1[1]-loc2[1])
      total += (dx+dy) * i
    
    return total

  def __eq__(self, other):
    for (i, row) in enumerate(other.data):
      for (j, num) in enumerate(row):
        if num != self.data[i][j]:
          return False
    return True
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self)

class Node:
  def __init__(self, state: State, depth: int, cost: int, parent, action: Action):
    self.state = state
    self.parent = parent
    self.action = action
    self.cost = cost
    self.depth = depth
  
  def generate_childeren(self) -> list:
    childeren = []

    for action in self.state.valid_actions():
      childeren.append(Node(
        self.state.apply_action(action),
        self.depth + 1,
        self.cost + action.num,
        self,
        action))
    return childeren
  
  def __str__(self):
    return f'< state = {self.state}, action = {self.action}, g(n) = {self.cost}, d = {self.depth}, parent = {self.parent}>'

def print_result(node: Node, stats: Stats):
  print('Nodes Popped: %d' % (stats.nodes_popped))
  print('Nodes Expanded: %d' % (stats.nodes_expanded))
  print('Nodes Generated: %d' % (stats.nodes_generated))
  print('Max Fringe Size: %d' % (stats.max_fringe_size))
  print('Solution Found at depth %d with cost of %d.' % (node.depth, node.cost))
  print('Steps: ')

  actions = ''
  cur_node = node
  while cur_node.action is not None:
    actions = f'    {cur_node.action}\n' + actions
    cur_node = cur_node.parent
  print(actions)

def bfs_search(start_state: State, goal_state: State, logger: Logger):
  stats = Stats()

  fringe = []
  closed = []

  # add first node
  fringe.append(Node(start_state, depth=0, cost=0, parent=None, action=None))
  stats.generated_nodes(1)

  while len(fringe) != 0:
    stats.update_max_fringe_size(len(fringe))

    # pop first node fifo style
    cur_node = fringe.pop(0)
    stats.popped_node()

    # if already visited, skip
    if cur_node.state in closed:
      continue
    
    # if goal state, return
    if cur_node.state.__eq__(goal_state):
      print_result(cur_node, stats)
      logger.log_success(cur_node, stats)

      return 0
    
    # add to closed
    closed.append(cur_node.state)

    # generate childeren
    childeren = cur_node.generate_childeren()
    fringe += childeren
    stats.expanded_node()
    stats.generated_nodes(len(childeren))

    logger.log_successors(cur_node, len(childeren))
    logger.log_closed(closed)
    logger.log_fringe(fringe)

  print('No solution found.')
    
  return 0
def ucs_search(start_state: State, goal_state: State, logger: Logger):
  stats = Stats()

  fringe = []
  closed = []

  # add first node
  fringe.append(Node(start_state, depth=0, cost=0, parent=None, action=None))
  stats.generated_nodes(1)

  while len(fringe) != 0:
    stats.update_max_fringe_size(len(fringe))

    # pop first node
    cur_node = fringe.pop(0)
    stats.popped_node()

    # if already visited, skip
    if cur_node.state in closed:
      continue
    
    # if goal state, return
    if cur_node.state.__eq__(goal_state):
      print_result(cur_node, stats)
      logger.log_success(cur_node, stats)

      return 0
    
    # add to closed
    closed.append(cur_node.state)

    # generate childeren
    childeren = cur_node.generate_childeren()
    fringe += childeren
    fringe.sort(key = lambda node: node.cost) # sort by cost

    stats.expanded_node()
    stats.generated_nodes(len(childeren))

    logger.log_successors(cur_node, len(childeren))
    logger.log_closed(closed)
    logger.log_fringe(fringe)

  print('No solution found.')
    
  return 0
def greedy_search(start_state: State, goal_state: State, logger: Logger):
  stats = Stats()

  fringe = []
  closed = []

  # add first node
  fringe.append(Node(start_state, depth=0, cost=0, parent=None, action=None))
  stats.generated_nodes(1)

  while len(fringe) != 0:
    stats.update_max_fringe_size(len(fringe))

    # pop first node fifo style
    cur_node = fringe.pop(0)
    stats.popped_node()

    # if already visited, skip
    if cur_node.state in closed:
      continue
    
    # if goal state, return
    if cur_node.state.__eq__(goal_state):
      print_result(cur_node, stats)
      logger.log_success(cur_node, stats)

      return 0
    
    # add to closed
    closed.append(cur_node.state)

    # generate childeren
    childeren = cur_node.generate_childeren()
    fringe += childeren
    fringe.sort(key = lambda node: node.state.heuristic(goal_state)) # sort by cost

    stats.expanded_node()
    stats.generated_nodes(len(childeren))

    logger.log_successors(cur_node, len(childeren))
    logger.log_closed(closed)
    logger.log_fringe(fringe)

  print('No solution found.')
    
  return 0
def a_search(start_state: State, goal_state: State, logger: Logger):
  stats = Stats()

  fringe = []
  closed = []

  # add first node
  fringe.append(Node(start_state, depth=0, cost=0, parent=None, action=None))
  stats.generated_nodes(1)

  while len(fringe) != 0:
    stats.update_max_fringe_size(len(fringe))

    # pop first node fifo style
    cur_node = fringe.pop(0)
    stats.popped_node()

    # if already visited, skip
    if cur_node.state in closed:
      continue
    
    # if goal state, return
    if cur_node.state.__eq__(goal_state):
      print_result(cur_node, stats)
      logger.log_success(cur_node, stats)

      return 0
    
    # add to closed
    closed.append(cur_node.state)

    # generate childeren
    childeren = cur_node.generate_childeren()
    fringe += childeren
    fringe.sort(key = lambda node: node.cost + node.state.heuristic(goal_state)) # sort by cost

    stats.expanded_node()
    stats.generated_nodes(len(childeren))

    logger.log_successors(cur_node, len(childeren))
    logger.log_closed(closed)
    logger.log_fringe(fringe)

  print('No solution found.')
    
  return 0

def dfs_search(start_state: State, goal_state: State, logger: Logger):
  print('Not implemented.')
    
  return 0
def dls_search(start_state: State, goal_state: State, logger: Logger):
  print('Not implemented.')
    
  return 0
def ids_search(start_state: State, goal_state: State, logger: Logger):
  print('Not implemented.')
    
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

  # logger setup
  match dump_flag.lower():  
    case "true":
      dump_flag = True
    case "false":
      dump_flag = False
    case _:
      print('Invalid dump flag. Choose from:\ntrue, or false')
      return 1
  logger = Logger(dump_flag, 'dump.log')
  logger.log_args(sys.argv)
  
  # file io
  start_state = State.from_file(start_file)
  goal_state = State.from_file(goal_file)

  # method matching
  method = method.lower()
  match method:
    case "bfs":
      logger.log_method(method)
      bfs_search(start_state, goal_state, logger)
    case "ucs":
      logger.log_method(method)
      ucs_search(start_state, goal_state, logger)
    case "dfs": # optional
      logger.log_method(method)
      dfs_search(start_state, goal_state, logger)
    case "dls": # optional
      logger.log_method(method)
      dls_search(start_state, goal_state, logger)
    case "ids": # optional
      logger.log_method(method)
      ids_search(start_state, goal_state, logger)
    case "greedy":
      logger.log_method(method)
      greedy_search(start_state, goal_state, logger)
    case "a*":
      logger.log_method(method)
      a_search(start_state, goal_state, logger)
    case _:
      print('Invalid method type. Choose from:\nbfs, ucs, dfs, dls, ids, greedy, or a*')
      return 1
    
  return 0

if __name__ == "__main__":
  main()