import sys

def graph_search(method, dump_flag): # change parameters as needed
  if dump_flag:
    print(method, dump_flag)
    
  return 0

def goal_test():
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

  match dump_flag.lower():  # dump flag matching
    case "true":
      dump_flag = True
    case "false":
      dump_flag = False
    case _:
      print('Invalid dump flag. Choose from:\ntrue, or false')
      return 1
        
  match method.lower(): # method matching
    case "bfs":
      graph_search(method, dump_flag) # change parameters as needed
    case "ucs":
      graph_search(method, dump_flag)
    case "dfs": # optional
      graph_search(method, dump_flag)
    case "dls": # optional
      graph_search(method, dump_flag)
    case "ids": # optional
      graph_search(method, dump_flag)
    case "greedy":
      graph_search(method, dump_flag)
    case "a*":
      graph_search(method, dump_flag)
    case _:
      print('Invalid method type. Choose from:\nbfs, ucs, dfs, dls, ids, greedy, or a*')
      return 1
    
  return 0

if __name__ == "__main__":
  main()