import numpy as np
from uci_data import *

def normalize(training_inputs, test_inputs):
  # TODO: normalize dimensions with F(v) = (v - mean) / std. if std == 0, std = 1 instead. mean and std come from training data
  return (training_inputs, test_inputs)

def knn_classify(training_file, test_file, k):
  # input / unpacking
  (training_set, test_set, label_int_conversions) = read_uci_dataset(training_file, test_file)
  (training_inputs, training_labels) = training_set
  (test_inputs, test_labels) = test_set
  (labels_to_ints, ints_to_labels) = label_int_conversions

  # normalizing
  (training_inputs, test_inputs) = normalize(training_inputs, test_inputs)
  
  # TODO
  # for each entry in test_set
  #   get k nearest neighbors, predict the most common one
  #   print('ID=%5d, predicted=%10s, true=%10s, accuracy=%4.2f' % (object_id, predicted_class, true_class, accuracy))

  # TODO
  # print('classification accuracy=%6.4f' % (classification_accuracy))
  pass