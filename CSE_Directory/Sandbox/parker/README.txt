Parker Steach
1001843388
README for project 2 Distance Vector Routing

input files for setting up nodes and edges:
    - each link should be up as the example from the lab 2 document
    - make sure each value is separated by a space
    - nodes can ONLY be numbers 1-6, anything else for the first two values on the line in the input file will be ignored
        - if the node id's are letters or anything else, they will be ignored and probably cause issues with the code
        - if file selected for input contains nodes for anything greater than 7 or less than 1, they will be ignored    

if there is no edge between two nodes, the value will be sent to -1     

running the code:
0) there are no special libraries used, user should be able to run DV_routing.py into terminal
1) user will enter the name of file for router connections in the terminal
    1.5)if the file cannot be found the code will stop and user will have to rerun the python file
2) after the file is opened and read a GUI should appear to the user
3) here you should see all nodes, their connections, costs, and paths
step-through
4) if the user selects 'step through routing', the table will update HOWEVER, for some reason it takes a second for the threads to finish, so watch the terminal for a phrase "continue". Once the phrase has appeared in the terminal you are safe to select another button
    4.5) I tried figuring out a way to prevent the user from pressing the button while the function is running but it just caused problems...
5)if the user decides to step through all the way, when the table is stable, there will be a line of text above the buttons to notify the user and inform them how many cycles it took
run-through
6) if the user selects 'run through routing' the code will go all the way until a stable state is reached,
7) when a stable state is reached, text above the buttons will notify the user stability has been achieved and provide the time it took to achieve stability

8)To close the progam the user MUST type 'exit' into the terminal at any time
NOTE: closing the GUI will not terminate the program
- if anything weird happens during calculations such as errors, close the program and try again, sometimes I've had weird issues where it just didn't run, should be very unlikely