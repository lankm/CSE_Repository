def map():
  print("SOL")
  print("O-o-o-o-o-o-o")
  print("    : . : . .")
  return 0

while(True):
  print("> ", end="")
  str = input()
  match str:
    case "map":
      map()
    case _:
      break