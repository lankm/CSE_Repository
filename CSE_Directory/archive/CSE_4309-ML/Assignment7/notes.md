# Lecture 1: Oct-27

## Slides 1

map is 2d array. with reachable/unreachable states and some terminals cells. terminals provide positive/negative rewards.
A 'mission' is traveling from one position to a terminal while prioritizing positive rewards.
multiple terminals are achived by executing multiple missions.
non-terminal cells can also have positive/negative rewards.

utility is the sum of rewards over a mission.
reward is the weight of only one action.

actions are non-deterministic. (trivial if it wasn't)

if a non-deterministic action causes an action into a wall, nothing happens
'markov' processes generally mean that nothing matters other than the current state and the action. histoy of states has no effect.
a look-up table or a function can be used to correlate the probability of resultant states given the current state and action taken: 
  p((1,1)|(1,1),'left') = 0.9 because both going left (.8) and going down (.1) result in hitting a wall

# Lecture 2: Oct-30

## Slides 1

discounted additive rewards: reduse the weight of future rewards towards the utility because future actions become less likely due to unknown factors.

policy: maps states to actions. optimal policies maximizes the expected utility

## Slides 2

utility is usually used for a set of states with actions between them. We can extend this definition to just one state by following the optimal policy from that state to a terminal state.

The problem with this is that there are an infinite amount of possible sets of states because actions are non-deterministic

# Lecture 3: Nov-1

## Slides 2

We can avoid having to solve for an infinite amount of possible states by just focusing on probabilities of a possible optimal policy. In the example problem we are given, we have only four possible actions; assume an action is the optimal policy, calculate its weighted expected utility, compare to other possible optimal policies. The weighted expected utility would look something like:

U(1,1) = 0.8\*0.86 + 0.1\*(-0.94) + 0.1\*X

U(1,1) = 0.8\*0.86 + 0.1\*(-0.94) + 0.1\*(-0.04 + gamma\*U(1,1))

U(1,1) = 0.594 - 0.004 + 0.1\*0.9\*U(1,1)

0.91\*U(1,1) = 0.590

U(1,1) = 0.590/0.91 = 0.648

This process is formalized in the Bellman equation.

# Lecture 4: Nov-3

## Slides 3

The bellman equation is non-linear because it contains a max function.