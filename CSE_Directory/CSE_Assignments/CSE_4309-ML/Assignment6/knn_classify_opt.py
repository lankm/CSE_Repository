import numpy as np
from uci_data import *


def L1(test_input, training_inputs):
  delta = np.abs(np.subtract(test_input, training_inputs))
  return np.sum(delta, axis = 1)
def L2(test_input, training_inputs):
  delta = np.subtract(test_input, training_inputs)
  return np.sqrt(np.sum(np.square(delta), axis = 1))

def normalize(training_inputs, test_inputs):
  # mean
  training_means = np.mean(training_inputs, axis = 0)

  # std
  training_stds = np.std(training_inputs, axis = 0, ddof = 1)
  training_stds[training_stds == 0] = 1

  # apply F(v) = (v-mean)/std
  training_inputs = np.divide(np.subtract(training_inputs, training_means),training_stds)
  test_inputs     = np.divide(np.subtract(test_inputs,     training_means),training_stds)

  return (training_inputs, test_inputs)

def knn_classify(training_file, test_file, k, dist_opt=1):
  dist = L1 if(dist_opt==1) else L2

  # input / unpacking
  (training_set, test_set, label_int_conversions) = read_uci_dataset(training_file, test_file)
  (training_inputs, training_labels) = training_set
  (test_inputs, test_labels) = test_set
  (labels_to_ints, ints_to_labels) = label_int_conversions

  # normalize
  (training_inputs, test_inputs) = normalize(training_inputs, test_inputs)

  accuracies = []
  for (i, test_input) in enumerate(test_inputs):
    # calculating knn
    distances = dist(test_input, training_inputs)
    knn_idx = np.argsort(distances)[:k]
    knn_labels = training_labels[knn_idx]

    # calculating weight of each class
    unique = np.unique(knn_labels)
    weights = np.zeros(len(unique))
    for (j, cla) in enumerate(unique): # weighing the classes by inverse distance
      for (l, weight) in enumerate(np.divide(1, distances[knn_idx])):
        if(training_labels[knn_idx][l] == cla):
          weights[j] += weight

    # predicting class
    largest_count_idx = np.argmax(weights)
    largest_count = weights[largest_count_idx]
    predicted_class = unique[largest_count_idx]

    # eliminating non-ties
    unique = unique[weights == largest_count]
    weights = weights[weights == largest_count]

    # accuracy calculation
    accuracy = 0
    if test_labels[i] in unique:
      accuracy = 1 / len(unique)
    accuracies.append(accuracy)

    # output
    print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f' % 
          (i+1, 
           ints_to_labels[predicted_class], 
           ints_to_labels[test_labels[i]],
           accuracy))
    
  classification_accuracy = sum(accuracies)/len(accuracies)
  print('classification accuracy=%6.4f' % (classification_accuracy))  
