from abc import ABC, abstractmethod
from enum import Enum
import sys
import copy

class Choice(Enum):
  TAKE_RED = 'red'
  TAKE_BLUE = 'blue'

  def choose_lowest(num_red, num_blue):
    if num_red < num_blue:
      return Choice.TAKE_RED
    else:
      return Choice.TAKE_BLUE 
  def choose_highest(num_red, num_blue):
    if num_red > num_blue:
      return Choice.TAKE_RED
    else:
      return Choice.TAKE_BLUE

class Nim_game:
  def __init__(self, num_red, num_blue, version, players):
    self.num_red = num_red
    self.num_blue = num_blue
    self.version = version
    self.players = players
    self.num_turn = 0

  def run_game(self):
    while True:
      if self.ending_condition():
        return self.end_game()
      else:
        self.run_turn()
  def end_game(self):
    player = self.get_player()
    other_player = self.get_other_player()
    score = self.score_game()

    if score < 0:
      print(f'The {other_player} wins by {-score}.')
      return other_player.__str__()
    elif score > 0:
      print(f'The {player} wins by {score}.')
      return player.__str__()
    else:
      print(f'It is a tie.') # This should not happen
      return None
  def run_turn(self):
    player = self.get_player()
    choice = player.take_turn( self.num_red, self.num_blue, self.version)

    match choice:
      case Choice.TAKE_RED:
        self.take_red()
      case Choice.TAKE_BLUE:
        self.take_blue()

  def take_red(self):
    self.num_red -= 1
    self.num_turn += 1
    return self
  def take_blue(self):
    self.num_blue -= 1
    self.num_turn += 1
    return self

  def get_player(self):
    return self.players[ self.num_turn % 2 ]
  def get_other_player(self):
    return self.players[ (self.num_turn + 1) % 2 ]

  def ending_condition(self):
    if self.num_blue == 0 or self.num_red == 0:
      return True
    else:
      return False
  def score_game(self):
    base_value = 2*self.num_red + 3*self.num_blue
    return base_value if self.is_misere() else -base_value

  def is_standard(self):
    return self.version == 'standard'
  def is_misere(self):
    return not self.is_standard()

  def has_odd_marbles(self):
    return (self.num_blue + self.num_red) % 2 == 1
  def has_even_marbles(self):
    return (self.num_blue + self.num_red) % 2 == 0

class Player(ABC):
  @abstractmethod
  def take_turn(self, num_red, num_blue, version) -> Choice:
    pass
  @abstractmethod
  def __str__(self) -> str:
    pass

  def __repr__(self):
    return str(self)


class Human(Player):
  def __init__(self, name):
    self.name = name
    None

  def take_turn(self, num_red, num_blue, version) -> Choice:
    print(f'There are {num_red} red marbles.')
    print(f'There are {num_blue} blue marbles.')
    print(f'Which pile do you take from: ')

    while True:
      user_input = input().lower()

      if 'red' in user_input and 'blue' in user_input:
        print('Found both "red" and "blue" in your choice. Please select one:')
        continue
      if 'red' in user_input:
        return Choice.TAKE_RED
      elif 'blue' in user_input:
        return Choice.TAKE_BLUE
      else:
        print('Expected a choice with "red" or "blue". Please select one:')
        continue


  def __str__(self) -> str:
    return f'{self.name}'


class Computer(Player):
  def __init__(self, depth, name):
    self.name = name
    self.depth = depth

  def take_turn(self, num_red, num_blue, version) -> Choice:
    # assume we are playing against an optimal opponent
    players = (self, Computer(self.depth, "other computer"))
    current_state = Nim_game(num_red, num_blue, version, players)
    (choice, value) = self.min_max(current_state, -sys.maxsize - 1, sys.maxsize, 0)
    
    print(f'The computer takes a {choice.value} marble.')
    return choice
  
  def min_max(self, current_state, alpha, beta, depth) -> Choice:
    # game ends
    if current_state.ending_condition():
      value = current_state.score_game()
      # print(f'{"  "*depth}{self.name}: ({current_state.num_red}, {current_state.num_blue}) val: {value} ({alpha}, {beta})') # DEBUG
      return (None, value)

    # depth limit reached
    if depth >= self.depth:
      (choice, value) = Computer.eval_fn(current_state)
      # print(f'{"  "*depth}{self.name}: ({current_state.num_red}, {current_state.num_blue}) val: {value} ({alpha}, {beta})') # DEBUG
      return (choice, value)
    
    # print(f'{"  "*depth}{self.name}: ({current_state.num_red}, {current_state.num_blue}) ({alpha}, {beta})') # DEBUG
    
    state_of_taking_red = copy.deepcopy(current_state).take_red()
    state_of_taking_blue = copy.deepcopy(current_state).take_blue()

    # order defined in assignment description
    other_player = current_state.get_other_player()
    if current_state.is_standard():
      (choice, take_blue_value) = other_player.min_max(state_of_taking_blue, -beta, -alpha, depth+1)
      take_blue_value = -take_blue_value # negate because it is what the other player wants

      # pruning if needed
      alpha = max(alpha, take_blue_value)
      if alpha < beta:
        (choice, take_red_value) = other_player.min_max(state_of_taking_red, -beta, -alpha, depth+1)
        take_red_value = -take_red_value # negate because it is what the other player wants
      else:
        return (Choice.TAKE_BLUE, take_blue_value)
      
    else:
      (choice, take_red_value) = other_player.min_max(state_of_taking_red, -beta, -alpha, depth+1)
      take_red_value = -take_red_value # negate because it is what the other player wants

      # pruning if needed
      alpha = max(alpha, take_red_value)
      if alpha < beta:
        (choice, take_blue_value) = other_player.min_max(state_of_taking_blue, -beta, -alpha, depth+1)
        take_blue_value = -take_blue_value # negate because it is what the other player wants
      else:
        return (Choice.TAKE_RED, take_red_value)
      
    # choose the optimal choice
    if take_red_value > take_blue_value:
      return (Choice.TAKE_RED, take_red_value)
    else:
      return (Choice.TAKE_BLUE, take_blue_value)

  def eval_fn(current_state):
    if current_state.is_misere():
        scale = 1 if current_state.has_odd_marbles() else -1

        if current_state.num_red == 1 or current_state.num_blue == 1:
          choice = Choice.choose_highest(current_state.num_red, current_state.num_blue)
        else:
          choice = Choice.choose_lowest(current_state.num_red, current_state.num_blue)

        return (choice, scale)
      
    else:
      scale = 1 if current_state.has_even_marbles() else -1

      if current_state.num_red == 1 or current_state.num_blue == 1:
        choice = Choice.choose_lowest(current_state.num_red, current_state.num_blue)
      elif current_state.num_red == 2 or current_state.num_blue == 2:
        choice = Choice.choose_highest(current_state.num_red, current_state.num_blue)
      else:
        choice = Choice.choose_lowest(current_state.num_red, current_state.num_blue)

      return (choice, scale)

  def __str__(self) -> str:
    return f'{self.name}'


def main():
  argc = len(sys.argv)

  # NUMBER PARAMETERS
  if argc < 3:
    print('Expected:\nred_blue_nim.py <num-red> <num-blue> <version?> <first-player?> <depth?>')
    return 1

  num_red = sys.argv[1]
  if not num_red.isnumeric():
    print("Expected <num-red> to be an integer")
    return 1
  num_red = int(num_red)
  
  num_blue = sys.argv[2]
  if not num_blue.isnumeric():
    print("Expected <num-blue> to be an integer")
    return 1
  num_blue = int(num_blue)

  # VERSION PARAMETER
  version = 'standard'
  if argc > 3:
    version = sys.argv[3] # stanard or misere
  
  version = version.lower()
  match version:
    case "standard": None
    case "misere": None
    case _:
      print("Expected <version>: standard, misere")
      return 1

  # FIRST_PLAYER PARAMETER
  first_player = 'human'
  if argc > 4:
    first_player = sys.argv[4]

  first_player = first_player.lower()
  match first_player:
    case "computer": None
    case "human": None
    case _:
      print("Expected <first-player>: computer, human")
      return 1

  # FIRST_PLAYER PARAMETER
  depth = '100000'
  if argc > 5:
    depth = sys.argv[5]
  
  if not depth.isnumeric():
    print("Expected <depth> to be an integer")
    return 1
  depth = int(depth)

  # GAME INITIALIZATION
  players = ( Human('human'), Computer(depth, 'computer') ) if first_player == 'human' else ( Computer(depth, 'computer'), Human('human') )
  nim_game = Nim_game(num_red, num_blue, version, players)
  nim_game.run_game()

  return 0

if __name__ == "__main__":
  main()