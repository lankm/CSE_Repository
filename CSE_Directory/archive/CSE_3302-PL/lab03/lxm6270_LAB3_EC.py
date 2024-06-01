# Author: Landon Moon
# ID: 1001906270
#
# added ^ and % as opperators

import fileinput

opps = {'+','-','*','/','^','%'}                                      # valid opperators
evaluate = {                                                          # opperator -> opperation
  '+': lambda a, b: a+b,
  '-': lambda a, b: a-b,
  '*': lambda a, b: a*b,
  '/': lambda a, b: a/b,
  '^': lambda a, b: a**b,
  '%': lambda a, b: a%b
}

for line in fileinput.input(files ='input_RPN_EC.txt'):                  # for each line
  toks = line.split()                                                 # tokenize
  try:
    while i:=[i for i, item in enumerate(toks) if item in opps][0]:   # while next opperator exists
      val = evaluate[toks[i]]( float((toks[i-2])), float(toks[i-1]) ) # evaluate
      toks[i] = str(val)                                              #}
      del toks[i-1]                                                   #}replace
      del toks[i-2]                                                   #}

  except:
    if len(toks)!=1:                                                  # if invalid
      print("Invalid expression.")
    else:                                                             # if valid
      print(toks[0])
