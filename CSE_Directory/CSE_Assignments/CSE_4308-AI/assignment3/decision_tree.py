import numpy as np
from uci_data import *
import random # used in choose_random_attribute
import sys
import threading

class Node:
  def __init__(self, attribute, threshold, gain, distribution):
    self.attribute = attribute
    self.threshold = threshold
    self.gain = gain
    self.distribution = distribution

# =============================================================================
def training(training_set, option, pruning_thr, threshold_cnt):
  (training_inputs, training_labels) = training_set

  global choose_attribute
  if type(option) == int: # decision forrest
    num_trees = option
    choose_attribute = choose_random_attribute
  else: # single tree
    num_trees = 1
    choose_attribute = choose_optimal_attribute

  trees = []
  threads = []
  for i in range(num_trees):
    tree = {}
    trees.append(tree)

    t = threading.Thread(target=dtl, args=(1, training_set, get_distribution(training_labels), tree))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()


  return trees

def dtl(root_id, examples, distribution, tree):
  # extracting variables
  global choose_attribute
  global THRESHOLD_CNT
  global PRUNING_THR
  (example_inputs, example_labels) = examples

  if len(example_labels) < PRUNING_THR:
    tree.update({ root_id: Node(-1, -1, 0, distribution) })
  elif get_entropy(example_labels) == 0:
    tree.update({ root_id: Node(-1, -1, 0, get_distribution(example_labels)) })
  else:
    (best_gain, best_attribute, best_threshold) = choose_attribute(examples, THRESHOLD_CNT)
    
    # splitting examples
    attribute_values = example_inputs[:,best_attribute]
    left_indexes =  attribute_values <  best_threshold 
    examples_left = ( example_inputs[left_indexes], example_labels[left_indexes] )
    right_indexes = attribute_values >= best_threshold
    examples_right = ( example_inputs[ right_indexes ], example_labels[right_indexes] )

    # adding subnodes
    tree.update({ root_id: Node(best_attribute, best_threshold, best_gain, distribution) })
    dtl(2*root_id,   examples_left, get_distribution(example_labels), tree)
    dtl(2*root_id+1, examples_right,  get_distribution(example_labels), tree)
def get_distribution(labels):
  (unique, counts) = np.unique(labels, return_counts=True)
  total = sum(counts)

  normalized = list(map(lambda count: count/total, counts))
  return dict( zip(unique, normalized) )

def choose_optimal_attribute(examples, threshold_cnts):
  (example_inputs, example_labels) = examples

  # iterating through possible attributes
  best_gain = -1
  for attribute in range( len(example_inputs[0]) ):
    (gain, threshold) = choose_best_threshold(examples, attribute, threshold_cnts)
    if gain > best_gain:
      best_gain = gain
      best_attribute = attribute
      best_threshold = threshold

  return (best_gain, best_attribute, best_threshold)
def choose_random_attribute(examples, threshold_cnts):
  (example_inputs, example_labels) = examples

  attribute = random.randint(0, len(example_inputs[0])-1)
  (best_gain, best_threshold) = choose_best_threshold(examples, attribute, threshold_cnts)
  return (best_gain, attribute, best_threshold)
def choose_best_threshold(examples, attribute, threshold_cnts):
  (example_inputs, example_labels) = examples
  attribute_values = example_inputs[:,attribute]

  # lower and upper bounds
  L = min(attribute_values)
  M = max(attribute_values)

  # iterating through possible thresholds
  best_gain = -1
  for K in range(threshold_cnts):
    threshold = L + K*(M-L)/(threshold_cnts+1)
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

def print_trees(trees):
  for (tree_id, tree) in enumerate(trees):
    for (node_id, node) in sorted(tree.items()):
      print("tree=%2d, node=%3d, feature=%2d, thr=%6.2f, gain=%f" % (tree_id+1, node_id, node.attribute, node.threshold, node.gain))

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

def print_results(results, ints_to_labels):
  for (object_id, predicted_class, true_class, accuracy) in results:
    predicted = ints_to_labels[predicted_class]
    true =      ints_to_labels[true_class]

    print("ID=%5d, predicted=%6s, true=%6s, accuracy=%4.2f" % (int(object_id), predicted, true, accuracy))

  classification_accuracy = np.mean(results[:,3])
  print("classigication accuracy=%6.4f" % (classification_accuracy))

# =============================================================================

def decision_tree(training_file, test_file, option, pruning_thr=1, threshold_cnt=50):
  # read dataset
  (training_set, test_set, label_int_conversions) = read_uci_dataset(training_file, test_file)
  (labels_to_ints, ints_to_labels) = label_int_conversions

  # set constant variables
  global PRUNING_THR
  PRUNING_THR = pruning_thr
  global THRESHOLD_CNT
  THRESHOLD_CNT = threshold_cnt

  # program execution
  trees = training(training_set, option, pruning_thr, threshold_cnt)
  print_trees(trees)

  results = classification(test_set, trees)
  print_results(results, ints_to_labels)

def main():
  argc = len(sys.argv)

  if argc < 4:
    print('Expected:\npython .\decision_tree.py <training_file> <test_file> <option>')
    return 1
  
  training_file = sys.argv[1]
  test_file = sys.argv[2]
  option = sys.argv[3]
  decision_tree(training_file, test_file, option)

if __name__ == "__main__":
  main()