import sys




def main():
  argc = len(sys.argv)

  if argc < 5:
    print('Expected:\nred_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>')
    return 1

  num_red = sys.argv[1]
  num_blue = sys.argv[2]
  version = sys.argv[3] # stanard or misere
  first_player = sys.argv[4] # computer or human. always between a computer and a human

  # num checking
  if not num_red.isnumeric():
    print("Expected <num-red> to be an integer")
    return 1
  num_red = int(num_red)
  
  if not num_blue.isnumeric():
    print("Expected <num-blue> to be an integer")
    return 1
  num_blue = int(num_blue)

  # version checking
  version = version.lower()
  match version:
    case "standard": None
    case "misere": None
    case _:
      print("Expected <version>: standard, misere")
      return 1
    
  # first_player checking
  first_player = first_player.lower()
  match first_player:
    case "computer": None
    case "human": None
    case _:
      print("Expected <first-player>: computer, human")
      return 1

  # TODO: depth cheching


  # computer - minmax with a b pruning
    # standard - move ordering is pick blue marble followed by pick red marble
    # misere - move ordering is pick red marble followed by pick blue marble
  # human - prompt to get move and perform it
  
  print("Stuff done.")

  return 0

if __name__ == "__main__":
  main()