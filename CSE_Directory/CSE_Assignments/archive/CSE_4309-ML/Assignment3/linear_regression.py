# README
# Program works as expected

import numpy as np

# gets phi as specified in the assignment description
def get_phi(dims: np.ndarray, degrees: int):
  phi = [1]
  for dim in dims:
    for degree in range(degrees):
      phi.append(pow(dim, degree+1))
  return np.array(phi)
# gets PHI
def get_PHI(inputs: np.ndarray, degrees: int):
  PHI = []
  for input in inputs:
    PHI.append(get_phi(input, degrees))
  return np.array(PHI)
# gets weight based on the equation on slide 44
def get_weights(PHI: np.ndarray, targets: np.ndarray, lambda1):
  return np.dot(
           np.dot(
             np.linalg.pinv(
               np.eye(len(PHI[0]))*lambda1 + np.dot(PHI.transpose(), PHI)
             ), PHI.transpose()
           ), targets
         )

# gets a file and puts it into memory
def memorize_file(filename, type):
  file = open(filename)
  lines = []
  for line in file.readlines():
    lines.append(list(map( type, line.split() )))
  return np.array(lines)

# calculates a value based on weights and basis functions
def evaluate(weights :np.ndarray, dims: np.ndarray, degrees: int):
  return np.dot( weights.transpose(), get_phi(dims, degrees) )



def linear_regression(training_file, test_file, degree, lambda1):

  # Training
  data = memorize_file(training_file, float)
  PHI = get_PHI(data[:, :-1], degree)
  weights = get_weights(PHI, data[:, -1], lambda1)

  for (i, weight) in enumerate(weights):
    print('w%d=%.4f' % (i, weight))
  
  # Testing
  data = memorize_file(test_file, float)
  for (i, line) in enumerate(data):
    output = evaluate(weights, line[:-1], degree)
    print('ID=%5d, output=%14.4f, target value = %10.4f, squared error = %.4f' % (i+1, output, line[-1], pow(line[-1]-output, 2)))

  return 0