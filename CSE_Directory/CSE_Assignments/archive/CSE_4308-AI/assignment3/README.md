Name: Landon Moon
ID: 1001906270
Language: Python 3.10.2

## preface
My submition for this assignment is an altered version of an assignment I did for my ML class. I checked with the AI professor and he said it is ok as long as I changed things up a bit. I've reformatted parts to conform to this assignment's requirements along with cleaning up the code.

# Code Structure
First and formost, the main function gets thre required arguments and gets them in a usable format for the rest of the program exectution. Memorizing the files is done primarily with a robust function I have from my ML class. I've cleaned it up a bit but otherwise it gets any UCI dataset and puts it into a numpy array. It also handles string type class labels.

The decision_tree() function is where the actual meat of the assignment is coordinated. This function executes and recieves a decision forest from training() then passes the trees and test_set to classification(). Lastly it prints the results from classification.

## training
First some argument handling is done. Because there is a possibility of having a decision forest, I format my data as a list of trees even if there is only one tree. Each tree is represented as a python dictionary (hashmap) where the key follows a pattern I'll explain in a bit, and the value is a node with the required information. The key is the ID of the node which corresponds to the iteration bredth-first-search would visit it. Otherwise the pseudo-code from the slides is followed. I implemented multiprocessing to speed up forest calculations.
### tree structure in-depth
As explained above, a decision tree is represented as a dictionary with corresponding keys. They keys are as follows:
- Root:  1
- Left:  2*cur_id
- Right: 2*cur_id + 1
This allows for quick and simple traversal of the tree without the need for implementing a tree structure manually.

## classification
Classificatin is straighforward; for each test entry, traverse the trees in the decision forest and combine into a probability distribution. Choose the most probable option for the result.

# How To Run
The code is implemented so run dtree.py with the expected arguments. Confirm that the files at the file locations actually exist. Examples:
- python dtree.py pendigits_training.txt pendigits_test.txt optimized
- python dtree.py pendigits_training.txt pendigits_test.txt randomized
- python dtree.py satellite_training.txt satellite_test.txt forest3
- python dtree.py yeast_training.txt yeast_test.txt forest15