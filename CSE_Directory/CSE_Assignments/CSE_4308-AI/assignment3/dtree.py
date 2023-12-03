import numpy as np              # utility functions
import random                   # random attribute
import sys, os                  # retrieving arguments and file IO
from multiprocessing import *   # speed up forest calculation

# tree structure is represented as a dictionary of nodes with keys corresponding to the bredth-first traversal ID of the tree.
class Node:
    def __init__(self, attribute, threshold, gain, distribution):
        self.attribute = attribute # -1 if leaf node
        self.threshold = threshold # -1 if leaf node
        self.gain = gain           #  0 if leaf node
        self.distribution = distribution

# training ====================================================================
def training(training_set, option):
    training_inputs, training_labels = training_set

    global choose_attribute
    match option:
        case 'optimized':
            num_trees = 1
            choose_attribute = choose_optimal_attribute
        case 'randomized':
            num_trees = 1
            choose_attribute = choose_random_attribute
        case 'forest3':
            num_trees = 3
            choose_attribute = choose_random_attribute
        case 'forest15':
            num_trees = 15
            choose_attribute = choose_random_attribute
        case _:
            raise ValueError('Invalid option')

    root_id = 1
    with Pool(num_trees) as p:
        CONSTS = (choose_attribute, THRESHOLD_CNT, PRUNING_THR) # passing consts is required due to multiprocessing
        params = [(root_id, training_set, get_distribution(training_labels), CONSTS)] * num_trees
        trees = list(p.starmap(dtl, params)) # List of dictionaries. Represents the forest.

    return trees

def dtl(root_id, examples, distribution, CONSTS):
    # extracting variables
    CHOOSE_ATTRIBUTE, THRESHOLD_CNT, PRUNING_THR = CONSTS
    example_inputs, example_labels = examples

    if len(example_labels) < PRUNING_THR:
        return { root_id: Node(-1, -1, 0, distribution) }
    elif get_entropy(example_labels) == 0:
        return { root_id: Node(-1, -1, 0, get_distribution(example_labels)) }
    else:
        best_gain, best_attribute, best_threshold = CHOOSE_ATTRIBUTE(examples, THRESHOLD_CNT)
    
        # splitting examples
        attribute_values = example_inputs[:,best_attribute]

        left_indexes =  attribute_values <  best_threshold 
        examples_left = ( example_inputs[left_indexes], example_labels[left_indexes] )

        right_indexes = attribute_values >= best_threshold
        examples_right = ( example_inputs[ right_indexes ], example_labels[right_indexes] )


        # adding subnodes
        tree = { root_id: Node(best_attribute, best_threshold, best_gain, distribution) } # self
        tree.update( dtl(2*root_id,   examples_left,  get_distribution(example_labels), CONSTS) ) # left
        tree.update( dtl(2*root_id+1, examples_right, get_distribution(example_labels), CONSTS) ) # right
        return tree
def get_distribution(labels):
    unique, counts = np.unique(labels, return_counts=True)
    total = sum(counts)

    normalized = list(map(lambda count: count/total, counts))
    return dict( zip(unique, normalized) )

def choose_optimal_attribute(examples, threshold_cnts):
    example_inputs, example_labels = examples

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
    # extracting variables
    example_inputs, example_labels = examples
  
    # select random attribute. get best threshold of that attribute
    attribute = random.randint(0, len(example_inputs[0])-1)
    best_gain, best_threshold = choose_best_threshold(examples, attribute, threshold_cnts)
    return (best_gain, attribute, best_threshold)
def choose_best_threshold(examples, attribute, threshold_cnts):
    example_inputs, example_labels = examples
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
    example_inputs, example_labels = examples
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
    unique, counts = np.unique(labels, return_counts=True)

    total = sum(counts)
    equation = lambda count: -(count/total)*np.log2(count/total)

    summation = sum(map(equation, counts))
    return summation

# classification ==============================================================
def classification(test_set, trees):
    test_inputs, test_labels = test_set

    results = np.empty((len(test_inputs),4))
    for (i, test_input) in enumerate(test_inputs):
        result = classify(test_input, test_labels[i], trees)
        results[i] = (i+1,) + result

    return results
def classify(test_input, test_label, trees):
    # iterating through all forests
    distribution_totals = {}
    for tree in trees:
        # traversing to a leaf node in tree
        node_id = 1
        cur_node = tree[node_id]
        while cur_node.attribute != -1: # while not leaf
            if test_input[cur_node.attribute] < cur_node.threshold:
                node_id = 2*node_id # go left
            else:
                node_id = 2*node_id+1 # go right
            cur_node = tree[node_id]

        # adding probabilities to total
        for (attribute, probability) in cur_node.distribution.items():
            distribution_totals[attribute] = distribution_totals.get(attribute, 0) + probability

    # select most probable choice
    predicted = max(distribution_totals, key=distribution_totals.get)

    accuracy = 0
    if predicted == test_label:
        num_duplicates = sum(bool(x) for x in list(distribution_totals.values()) == distribution_totals[predicted])
        accuracy = 1 / num_duplicates

    return (predicted, test_label, accuracy)

def print_results(results, ints_to_labels):
    for result in results:
        # extracting variables
        object_id, predicted_class, true_class, accuracy = result

        # string class name handling
        predicted = ints_to_labels[predicted_class]
        true =      ints_to_labels[true_class]

        print("Object Index=%5d, Result=%6s, True Class=%6s, Accuracy=%4.2f" % (int(object_id), predicted, true, accuracy))

    classification_accuracy = np.mean(results[:,3])
    print("Classification Accuracy=%6.4f" % (classification_accuracy))

# =============================================================================

def decision_tree(training_file, test_file, option, pruning_thr=50, threshold_cnt=50):
    # read dataset
    (training_set, test_set, label_int_conversions) = read_uci_dataset(training_file, test_file)
    (labels_to_ints, ints_to_labels) = label_int_conversions

    # set constant variables
    global PRUNING_THR
    PRUNING_THR = pruning_thr
    global THRESHOLD_CNT
    THRESHOLD_CNT = threshold_cnt


    # program execution
    trees = training(training_set, option)

    results = classification(test_set, trees)
    print_results(results, ints_to_labels)

# file memorization
def read_uci_file(pathname, labels_to_ints, ints_to_labels):
    if not(os.path.isfile(pathname)):
        raise ValueError(f'{pathname} not found')

    in_file = open(pathname)
    file_lines = in_file.readlines()
    in_file.close()

    rows = len(file_lines)
    if (rows == 0):
        raise ValueError(f'No rows in {pathname}')
        
    
    cols = len(file_lines[0].split())
    data = np.zeros((rows, cols-1))
    labels = np.zeros(rows)
    for row in range(0, rows):
        line = file_lines[row].strip()
        items = line.split()
        if (len(items) != cols):
            print("read_data: Line %d, %d columns expected, %d columns found" %(row, cols, len(items)))
            return None
        for col in range(0, cols-1):
            data[row][col] = float(items[col])
        
        # the last column is a string representing the class label
        label = items[cols-1]
        if (label in labels_to_ints):
            ilabel = labels_to_ints[label]
        else:
            ilabel = len(labels_to_ints)
            labels_to_ints[label] = ilabel
            ints_to_labels[ilabel] = label
        
        labels[row] = ilabel

    labels = labels.astype(int)
    return (data, labels)
def read_uci_dataset(training_file, test_file):
    labels_to_ints = {}
    ints_to_labels = {}

    training_set = read_uci_file(training_file, labels_to_ints, ints_to_labels)
    test_set = read_uci_file(test_file, labels_to_ints, ints_to_labels)
    return (training_set, test_set, (labels_to_ints, ints_to_labels))

def get_args():
    argc = len(sys.argv)

    if argc < 4:
        print('Expected:\npython .\decision_tree.py <training_file> <test_file> <option>')
        return 1
  
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    option = sys.argv[3]
    return training_file, test_file, option
def main():
    training_file, test_file, option = get_args()
    decision_tree(training_file, test_file, option)

if __name__ == "__main__":
  main()
