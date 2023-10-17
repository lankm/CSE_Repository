from abc import ABC, abstractmethod
from enum import Enum
import sys

class Choice(Enum):
  TAKE_RED = 1
  TAKE_BLUE = 2

class Nim_game:
  def __init__(self, num_red, num_blue, version, players):
    self.num_red = num_red
    self.num_blue = num_blue
    self.version = version
    self.players = players
    self.num_turn = 0

  def run_game(self):
    while True:
      if self.num_blue == 0 or self.num_red == 0:
        return self.end_game()
      else:
        self.run_turn()
  def end_game(self):
    player = Nim_game.get_player( self.players, self.num_turn )
    other_player = Nim_game.get_player( self.players, self.num_turn+1 )
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
    player = Nim_game.get_player(self.players, self.num_turn)
    choice = player.take_turn( self.num_red, self.num_blue )

    match choice:
      case Choice.TAKE_RED:
        self.take_red()
      case Choice.TAKE_BLUE:
        self.take_blue()
      
    self.num_turn += 1

  def take_red(self):
    self.num_red -= 1
  def take_blue(self):
    self.num_blue -= 1

  def get_player(players, num_turn):
    return players[ num_turn % 2 ]

  def score_game(self):
    base_value = 2*self.num_red + 3*self.num_blue
    return base_value if self.version == 'misere' else -base_value


class Player(ABC):
  @abstractmethod
  def take_turn(self, num_red, num_blue) -> Choice:
    pass
  @abstractmethod
  def __str__(self) -> str:
    pass

  def __repr__(self):
    return str(self)


class Human(Player):
  def __init__(self):
    None

  def take_turn(self, num_red, num_blue) -> Choice:
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
    return f'human'


class Computer(Player):
  def __init__(self, depth):
    self.depth = depth

  def take_turn(self, num_red, num_blue) -> Choice:
    # TODO: The actual assignment
    print(f'The computer takes a red marble.')
    return Choice.TAKE_RED

  def __str__(self) -> str:
    return f'computer'


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
  players = ( Human(), Computer(depth) ) if first_player == 'human' else ( Computer(depth), Human() )
  nim_game = Nim_game(num_red, num_blue, version, players)
  nim_game.run_game()

  return 0

if __name__ == "__main__":
  main()