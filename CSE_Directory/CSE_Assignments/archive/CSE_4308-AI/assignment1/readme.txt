Name & ID: Landon Moon 1001906270
Language: Python 3.10.11

I've completed all three of the extra credit algorithms.

==========STRUCTURE==========
The code is structure by having multiple helping classes. These classes are: stats, logger, action, state, and node. These classes implement all the details that are used by all the algorithms. The services provided by each class should be straight forward to understand but I'll give a general overview. Node, State, and Action all work together to represent the problem we are solving. A node represents a state with some extra information. A state is a single configuration of the board. Actions can be applied to States and States can generate valid actions. With these classes and functions, things like generating children in each algorithm is just a single function  call

The program starts in a main function that handles the arguments and does some simple error handling. The program arguments are then used to execute the coresponding search algorithms. The logger object is generated based on the dump_flag. This logger is then used in every algorith and either prints or doesn't print acording to the dump_flag. Each algoithm is a separate function; this is to make the code more readable. A lot of the functions could be compressed into one with flags, but that is less clear when reading. Each of the algorithms follow the algorithm shown in class almost perfectly, there are aditional comments in the code to make reading them easier.

dls is the only algorithm that really needs to be recursive so it is recursive. The code for it looks a bit messier because the services were build around the other functions. Aditionally some of the logging information like the actual fringe does not exist because of the recursive nature of dls. Instead just the relevent information about the closed, and children lists are printed.




==========HOW TO RUN==========
run a python script with the correct relative location to the start and goal files. The simplist solution is to run the python script within the same directory. Additionally, the method and dump_flag parameters are case insensitive for convienence. Examples include:
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt bfs 
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt a* true
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt ids
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt greedy true
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt

If dump_flag is true, a dump file will be made in the same directory called dump.log. Some algorithms such as ucs take a while to run but will eventually output. bfs and ucs are not instant so their dump files are giant. Unless you want to get zip-bombed, perferably don't run 'ucs true'

I have learned that some configurations of the problem that are unsolvable so if one of these start files are provided, the program will grow in memory size until all states are tested. dls is recursive so this memory explosion will cause a stack overflow error.

