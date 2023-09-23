Name & ID: Landon Moon 1001906270
Language: Python 3.10.11

==========STRUCTURE==========
The code is structure by having multiple helping classes. These classes are: stats, logger, action, state, and node. These classes implement all the details that are used by all the algorithms. The services provided by each class should be straigh forward to understand.

The program starts in a main function that handles the arguments and does some simple error handling. The program arguments are then used to execute the coresponding search algorithms. Each algoithm is a separate function; this is to make the code more readable. A lot of the functions could be compressed into one with flags, but that is less clear when reading.

==========HOW TO RUN==========
run a python script with the correct relative location to the start and goal files. The simplist solution is to run the python script within the same directory. Additionally, the method and dump_flag parameters are case insensitive. Examples include:
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt bfs 
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt a* true
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt ucs false
python .\expense_8_puzzle.py .\start_file.txt .\goal_file.txt greedy true

If dump_flag is true, a dump file will be made in the same directory called dump.log. Some algorithms such as ucs take a while to run but will eventually output. bfs and ucs are not instant so their dump files are giant. Unless you want to get zip-bombed perferably don't run 'ucs true'

I have learned that some configurations of the problem that are unsolvable so if one of these start files are provided, the program will grow in memory size untill all states are tested.

