# Grap Theory Project 2020
Write a program in Python to execute regular expressions on strings using the Thompson's construction algorithm.

# Structure
The project is broken into 3 files.
## NFA.py
contains two classes, Fragment and State.\
A Fragment class represents a nondeterministic finite automaton, a NFA has a start state and an accept state,
this s represented by the State class.

## Thompson.py
Contains the methods necessary for the Thompson's construction algorithm, shunt, compile, followes, match.
This class will also run a series of assertion tests when run.\
\
Shunt:\
Represents the shunting yard algorithm. Adds operators to a stack called opers,
otherwise characters are appended to the postfix list. Afterwards the opers stack is put onto the postfix list.\
The list is returned as a string.\
More information on the shunting yard algorithm found at https://brilliant.org/wiki/shunting-yard-algorithm/ \
\
Compile:\
Compiles the regex input into the NFA.\
The regex characters are turned into NFA fragments. Regex operators included are: catenation ('.'), alternation('|'), 
zero or more ('*'), zero or one ('?') and one or more ('+').\
More information on compiling regex expressions found at https://swtch.com/~rsc/regexp/regexp1.html \
\
Followes:\
Recursive function which adds a state to a set and follows all of the epsilon arrow.\
\
Match:\
Compiles the regex expression, loops through the string, if the label is equal to the character, add the state arrow to the current.\
Returns true if a match is found and false if not.

## Main.py
Allows for the user to enter a regex and string into the command line in the following format [regex, string].
Will accept 1 or 2 args. If 1 arg the string will be assumed to be empty.
