import numpy as np
from uci_data import *
import random # used in choose_random_attribute
import os # used for log_files

class Node:
  def __init__(self, attribute, threshold, gain, distribution):
    self.attribute = attribute
    self.threshold = threshold
    self.gain = gain
    self.distribution = distribution

# =============================================================================
def training(training_set, option, pruning_thr, num_threshold):
  (training_inputs, training_labels) = training_set

  if type(option) == int: # decision forrest
    num_trees = option
    choose_attribute = choose_random_attribute
  else: # single tree
    num_trees = 1
    choose_attribute = choose_optimal_attribute

  trees = []
  for i in range(num_trees):
    tree = dtl(1, training_set, (choose_attribute, num_threshold, pruning_thr), get_distribution(training_labels))
    trees.append(tree)

  return trees

def dtl(root_id, examples, CONSTANTS, distribution):
  # extracting variables
  (choose_attribute, num_threshold, pruning_thr) = CONSTANTS
  (example_inputs, example_labels) = examples

  if len(example_labels) < pruning_thr:
    return { root_id: Node(-1, -1, 0, distribution) }
  elif get_entropy(example_labels) == 0:
    return { root_id: Node(-1, -1, 0, get_distribution(example_labels)) }
  else:
    (best_gain, best_attribute, best_threshold) = choose_attribute(examples, num_threshold)
    
    # splitting examples
    attribute_values = example_inputs[:,best_attribute]
    left_indexes =  attribute_values <  best_threshold 
    examples_left = ( example_inputs[left_indexes], example_labels[left_indexes] )
    right_indexes = attribute_values >= best_threshold
    examples_right = ( example_inputs[ right_indexes ], example_labels[right_indexes] )

    # adding subnodes
    tree = { root_id: Node(best_attribute, best_threshold, best_gain, distribution) }
    tree.update(dtl(2*root_id,   examples_left, CONSTANTS, get_distribution(example_labels)))
    tree.update(dtl(2*root_id+1, examples_right, CONSTANTS, get_distribution(example_labels)))
    return tree
def get_distribution(labels):
  (unique, counts) = np.unique(labels, return_counts=True)
  total = sum(counts)

  normalized = list(map(lambda count: count/total, counts))
  return dict( zip(unique, normalized) )

def choose_optimal_attribute(examples, num_thresholds):
  (example_inputs, example_labels) = examples

  # iterating through possible attributes
  best_gain = -1
  for attribute in range( len(example_inputs[0]) ):
    (gain, threshold) = choose_best_threshold(examples, attribute, num_thresholds)
    if gain > best_gain:
      best_gain = gain
      best_attribute = attribute
      best_threshold = threshold

  return (best_gain, best_attribute, best_threshold)
def choose_random_attribute(examples, num_thresholds):
  (example_inputs, example_labels) = examples

  attribute = random.randint(0, len(example_inputs[0])-1)
  (best_gain, best_threshold) = choose_best_threshold(examples, attribute, num_thresholds)
  return (best_gain, attribute, best_threshold)
def choose_best_threshold(examples, attribute, num_thresholds):
  (example_inputs, example_labels) = examples
  attribute_values = example_inputs[:,attribute]

  # lower and upper bounds
  L = min(attribute_values)
  M = max(attribute_values)

  # iterating through possible thresholds
  best_gain = -1
  for K in range(num_thresholds):
    threshold = L + K*(M-L)/(num_thresholds+1)
    gain = get_information_gain(examples, attribute, threshold)
    if gain > best_gain:
      best_gain = gain
      best_threshold = threshold
  
  return (best_gain, best_threshold)

def get_information_gain(examples, attribute, threshold):
  (example_inputs, example_labels) = examples
  attribute_values = example_inputs[:,attribute]

  # extracing label sets
  less_labels =    example_labels[ attribute_values <  threshold ]
  greater_labels = example_labels[ attribute_values >= threshold ]

  # weights
  w2 = len(less_labels)/len(example_labels)
  w3 = len(greater_labels)/len(example_labels)


  # calculation
  e1 = get_entropy(example_labels)
  e2 = w2 * get_entropy(less_labels)
  e3 = w3 * get_entropy(greater_labels)

  return e1-e2-e3
def get_entropy(labels):
  (unique, counts) = np.unique(labels, return_counts=True)

  total = sum(counts)
  equation = lambda count: -(count/total)*np.log2(count/total)

  summation = sum(map(equation, counts))
  return summation

def print_trees(trees, log_file):
  for (tree_id, tree) in enumerate(trees):
    for (node_id, node) in sorted(tree.items()):
      str_node = f'tree={(tree_id+1):2d}, node={node_id:3d}, feature={node.attribute:2d}, thr={node.threshold:6.2f}, gain={node.gain:f}\n'
      print_and_log(str_node, log_file)
def get_log_file(directory, training_file, test_file, option, pruning_thr):
  training_file = os.path.basename(training_file)
  test_file = os.path.basename(test_file)

  if not os.path.exists(directory):
    os.mkdir(directory)

  file_name = f'{directory}/{training_file}-{test_file}-{option}-{pruning_thr}.log'
  return open(file_name, 'w')

# =============================================================================
def classification(test_set, trees):
  (test_inputs, test_labels) = test_set

  results = np.empty((len(test_inputs),4))
  for (i, test_input) in enumerate(test_inputs):
    result = classify(test_input, test_labels[i], trees)
    results[i] = (i+1,) + result

  return results
def classify(test_input, test_label, trees):
  # iterating through all forrests
  distribution_totals = {}
  for tree in trees:
    # traversing to end of a tree
    node_id = 1
    cur_node = tree[node_id]
    while cur_node.attribute != -1:
      if test_input[cur_node.attribute] < cur_node.threshold:
        node_id = 2*node_id
      else:
        node_id = 2*node_id+1
      cur_node = tree[node_id]

    # adding probabilities to total
    for (attribute, probability) in cur_node.distribution.items():
      distribution_totals[attribute] = distribution_totals.get(attribute, 0) + probability

  # select most probable choice
  predicted = max(distribution_totals, key=distribution_totals.get)

  accuracy = 0
  if predicted == test_label:
    num_duplicates = sum(bool(x) for x in list(distribution_totals.values())[:] == distribution_totals[predicted])
    accuracy = 1 / num_duplicates

  return (predicted, test_label, accuracy)

def print_results(results, log_file, ints_to_labels):
  for (object_id, predicted_class, true_class, accuracy) in results:
    predicted = ints_to_labels[predicted_class]
    true =      ints_to_labels[true_class]

    str_result = f'ID={int(object_id):5d}, predicted={predicted:6s}, true={true:6s}, accuracy={accuracy:4.2f}\n'
    print_and_log(str_result, log_file)

  classification_accuracy = np.mean(results[:,3])
  str_accuracy = f'classification accuracy={classification_accuracy:6.4f}\n'
  print_and_log(str_accuracy, log_file)

# =============================================================================
def print_and_log(str, log_file):
  print(str, end='')
  log_file.write(str)

def decision_tree(training_file, test_file, option, pruning_thr):
  # read dataset
  (training_set, test_set, label_int_conversions) = read_uci_dataset(training_file, test_file)
  (labels_to_ints, ints_to_labels) = label_int_conversions
  log_file = get_log_file('logs', training_file, test_file, option, pruning_thr)

  # program execution
  trees = training(training_set, option, pruning_thr, 50)
  print_trees(trees, log_file)

  results = classification(test_set, trees)
  print_results(results, log_file, ints_to_labels)