from decision_tree import *


# When you test your code, you can change this line to reflect where the 
# dataset directory is located on your machine.
dataset_directory = "../uci_data"

# When you test your code, you can select the dataset you want to use 
# by modifying the next lines
# dataset = "pendigits_string"
# dataset = "satellite_string"
dataset = "pendigits"


training_file = dataset_directory + "/" + dataset + "_training.txt"
test_file = dataset_directory + "/" + dataset + "_test.txt"

# When you test your code, you can select the function arguments you want to use 
# by modifying the next lines
option = "optimal"
# option = 1
# option = 3
# option = 15
pruning_thr = 50




decision_tree(training_file, test_file, option, pruning_thr)
