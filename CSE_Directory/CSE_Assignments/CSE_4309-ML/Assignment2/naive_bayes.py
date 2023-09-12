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

  # means and stds
  for key in raw_data:
    dim_data[key] = np.array([np.mean(raw_data[key], axis=0),
                              np.std(raw_data[key], axis=0, ddof=1)]).transpose()
    # correcting low stds
    for (i, dim) in enumerate(dim_data[key]):
      if dim[1] < 0.01:
        dim[1] = 0.01

  # calculating class probs
  class_probs = {}
  for key in class_totals:
    class_probs[key] = class_totals[key]/lines

  # raw_data should not be needed to be used
  return ( class_probs, dim_data )

def classification(class_probs, dim_data, test_file):
  results = []

  t_file = open(test_file, "rt")

  for (i, line) in enumerate(t_file.readlines()):
    line = line.split()

    line_class = int(line[-1]) # do not use
    line_dims = list(map(float, line[:-1]))
    # TODO calculate bayesian probs
    #P(x|C)... gaussians
    #p(C) = class_probs(c)
    #P(x)... sum rule

    #P(C|x) = P(x|C) * p(C) / P(x)

    predicted = 1
    probability = 1   # TODO replace dummy values
    accuracy = 1

    results.append([i+1, predicted, probability, line_class, accuracy])
  
  results = np.array(results)
  avg_accuracy = np.mean(results, axis=0)[4]

  return (results, avg_accuracy)


def naive_bayes(training_file, test_file):
  # training
  (class_probs, dim_data) = train(training_file)
  # class_probs[class]
  # dim_data[class][dim][ mean-0 / std-1 ]

  for key in sorted(list(dim_data.keys())):
    for (i,dim) in enumerate(dim_data[key]):
      print("Class %d, attribute %d, mean = %.2f, std = %.2f" % (key, i+1, dim[0], dim[1]))

  # classification
  (results, accuracy) = classification(class_probs, dim_data, test_file)
  # results[ ID-0 / predicted-1 / probability-2 / true-3 / accuracy-4 ]
  # accuracy

  for (i, result) in enumerate(results):
    print("ID=%5d, predicted=%3d, probability = %.4f, true=%3d, accuracy=%4.2f" % (result[0], result[1], result[2], result[3], result[4]))
  print("classification accuracy=%6.4f" % (accuracy))

  return 0