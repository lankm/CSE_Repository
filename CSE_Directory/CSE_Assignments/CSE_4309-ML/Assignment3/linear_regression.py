# README
# 


import numpy as np

def train(training_file):
  raw_data = {}
  dim_data = {}

  class_totals = {}
  lines = 0

  t_file = open(training_file, "rt")

  # bucketing all data
  for line in t_file.readlines():
    line = line.split()

    line_class = int(line[-1])
    line_dims = list(map(float, line[:-1]))

    if line_class not in raw_data:  #if doesn't exists
      raw_data[line_class] = [line_dims]
      class_totals[line_class] = 1
    else:                             #if aleady exists
      raw_data[line_class].append(line_dims)
      class_totals[line_class] += 1
    lines += 1

  # converting to numpy arrays
  for key in raw_data:
    raw_data[key] = np.array(raw_data[key])

  # calculating class probs
  class_probs = {}
  for key in class_totals:
    class_probs[key] = class_totals[key]/lines

  # raw_data should not be needed to be used
  return ( class_probs, raw_data )

def gausian(x, mean, std):
  return (1/(std*(2*np.pi)**(1/2))) * np.e**((-(x-mean)**2)/(2*std**2))

def classification(pC, dim_data, test_file):
  results = []

  t_file = open(test_file, "rt")

  for (i, line) in enumerate(t_file.readlines()):
    line = line.split()

    line_class = int(line[-1])
    line_dims = list(map(float, line[:-1]))

    # bayesian math
    
    PxC = {} #P(x|C)
    for cl in dim_data:
      PxC[cl] = 1
      for (j, dim) in enumerate(dim_data[cl]):
        mean = dim[0]
        std = dim[1]

        PxiC = gausian(line_dims[j], mean, std) #P(xi|C)

        PxC[cl] *= PxiC # product rule


    Px = 0 # P(x)
    for cl in PxC:
      Px += PxC[cl] * pC[cl] # sum rule

    # argmax bayes rule
    probability = 0
    predicted = []
    for cl in PxC:
      PCx = PxC[cl]*pC[cl]/Px # bayes rule

      if PCx > probability:
        probability = PCx
        predicted = [cl]

      elif PCx == probability:
        predicted.append(cl)

    accuracy = -1
    if line_class in predicted:
      accuracy = 1/len(predicted)
    else:
      accuracy = 0

    results.append([i+1, predicted[0], probability, line_class, accuracy])
  
  avg_accuracy =   avg_accuracy = np.mean(np.array(np.array(results)[:,4]), dtype=float)

  return (results, avg_accuracy)



def linear_regression(training_file, test_file, degree, lambda1):

  # degree - number of weights
  # lambda1 - value of lambda

  train(training_file)




  return 0