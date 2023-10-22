name: Landon Moon
ID: 1001906270

EXTRA CREDIT COMPLETED. look below.

Main sets up arguments and passes execution to a Nim_game class.

The code is structured into classes. There is a Nim_game class that represent the state and runtime of a game of nim as described in the description. There are additionaly a player class which can represent a human or a computer. These players are given to the Nim_game and take actions accordingly. The Nim_game is able to moderate/run itself through a function call which executes the game properly.

The human player is prompted to execute moves while the computer used alpha-beta-pruning. This function is done as a simulated game against an other optimal computer. The moves are simulated between the two computers with both chosing the best option for itself. This is done as a single function instead of muliple by negating the value from the other computer because its choice is the opposite of what the host computer would want. alpha-beta-pruning is done similary by fliping and negating alpha and beta between calls.


Lastly THE EXTRA CREDIT WAS COMPLETED. I discovered that an evaluation function for this specific problem is not needed because there is a defined choice based on parity. Anyway, the eval function that I chose summed up the amount of marbles left and used the total to determine if it should win. For misere it should win with an odd total, and for standard it should win for an even total. In either case, the computer believes that it can win or lose until it can see (min-max) that it might not be the case at a certain depth and with a set of choices. uncomment the debug statements, they give some insight into how it works.

Because a choice must be made for depth of 0, the choice taken follows from the eval function. For misere, the computer first gets one pile down to one and then hopes the player will take the last marble in the pile. For standard the computer does a similar thing but gets a pile down to two. Then once the player takes a marble, the computer can take one more and win. This choice does not matter any time the depth limit is not 0.




run the python script as intended. examples:
python .\red_blue_nim.py 10 11 misere human 0
python .\red_blue_nim.py 2 3 standard
python .\red_blue_nim.py 10 5 misere human 20
python .\red_blue_nim.py 9 3 misere computer 10

input validation is done in case typos or extra guidence is needed.