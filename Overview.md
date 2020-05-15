# Grap Theory Project 2020
Write a program in Python to execute regular expressions on strings using the Thompson's construction algorithm.

## Introduction
This program is an implementation of Thompson’s Construction algorithm using Python.  Thompson’s Construction algorithm is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). The NFA can then be used to perform pattern matching on strings.\
The code in this repository is contained within 3 files.
1)	NFA.py, represents an NFA.
2)	Thompson.py, contains the methods necessary for the Thompson's construction algorithm.
3)	Main.py, Allows for the user to enter command line arguments.


What is an automaton?\
An automaton is a machine which performs a range of functions according to a predetermined set of coded instructions. Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them.
The most standard variant, which is described above, is called a deterministic finite automaton (DFA). A DFA has the following components:\
1) Input: An DFA that accepts only finite sequence of symbols.
2) States: An DFA that contains only a finite number of states.
3) Transition: For a given current state and an input symbol, an NFA can only jump to one state.
4) Acceptance: Input is either accepted or rejected.

This program uses nondeterministic finite automaton (NFA) to compute a string of symbols. For each symbol it transitions to a new state until all inputs have been consumed. The machine can move to any combination of the states in the machine. In other words, the exact state to which the machine moves cannot be determined.\
\
How does an NFA differ from a DFA?\
In short, a DFA can best be described as one machine, whereas an NFA is like multiple machines performing computational activities at the same time. String rejection is notably different. In a DFA, string rejection occurs when the terminating state is other than the accepting state. In an NFA, rejection occurs only when all branches of the NFA are dead. An NFA is less limited than a DFA, it will traverse many paths for a given set of inputs and it can have many possible next states.


What is a regular expression?\
A regular expression (regex) is a text string which describes a search pattern. For example, any e-mail address can be found with the following regex ^ [A-Z0-9. _%+-] +@[A-Z0-9.-] +\. [A-Z] {2,} $ \
This allows the programmer to quickly search and find all e-mails. Regular expressions can be used to find just about any text pattern.

Converting a regular expression ((a.b) |c) * to an NFA:\
The brackets maintain standard mathematical operator precedence.\
The Kleene star (*) represents zero or more.\
The pipe symbol (|) represents logical OR.\
The decimal point symbol (.) represents concatenation. \
The expression ((a.b) |c) * can be understood as accepting zero or many ab or c. \
\
This following will illustrate how an NFA builds complexity out of simplicity.\
\
![Regex To NFA](https://github.com/eoinwilkie/Sem6_GraphTheoryAssessment/blob/master/img/RegexToNFA.png)

\
This program is created using the Python programming language. \
\
What is Python?\
Python is an interpreted, dynamically typed, object-orientated programming language.  It has gained popularity due to its simple syntax and an emphasizes on code readability.  Because of this design philosophy it is one of the easier programming languages to learn. Python also offers libraries, such as NumPy, an array processing package, OpenCV, a computer vision image processing package or TensorFlow, a machine learning library.  These libraries unlock the power of Python which is displayed through its widespread use in the areas of machine learning and big data. \
\
Installing Python\
A python installation guide for various Operating Systems can be found at https://realpython.com/installing-python/ \
\
Running the program\
The GitHub repository can be found at https://github.com/eoinwilkie/Sem6_GraphTheoryAssessment.git \
\
The program is run from the Main.py file. The user may enter arguments in the following ways,
1)	Regex followed by the string to be compared with.
2)	Regex followed by an empty string.
3)	Command line tools, which are prefixed with --.

\
## Test
To run by the Thompson.py file. This file also contains necessary algorithms for the program.  Tests are run by calling 	if __name__ = "__main__" \
This will run only if the class file is called with no arguments. This works because when Python reads a source file it will first define several variables, in this case the __name__ variable is assigned to the value “__main__”\
\
Tests are run to check for several scenarios, to test for catenation, catenation in combination with alternation and zero or more, further tests for catenation in combination with other operators exist within other testing sections.\
Zero or one tests are run in combination with alternation and zero or many.\
One or many tests are run in combination with alternation and zero or many.\
\
Tests are run by creating a data array and running a loop of assertion tests.\
\
\
## Algorithm
\
Shunt()\
The Shunting Yard Algorithm is the first step in Thompson’s Construction Algorithm, it is used to convert infix expressions to postfix expressions.\
The infix expression 4 + 18 / (9 − 3) would be converted to 4, 18, 9, 3, −, /, + \
This is done by parsing a list and placing the symbols on a stack or queue. Operators are placed on the operator stack and non-operators are placed on the output queue. Afterwards the operator stack is placed onto the output queue.\
\ 
![Shunting Yard Algorithm](https://github.com/eoinwilkie/Sem6_GraphTheoryAssessment/blob/master/img/ShuntingYard.png)


Compile()\
The compile function creates NFA structures out of the input symbols. Every NFA structure is as a fragment. Each fragment has a start state and an accept state.\
The default NFA’s start state is the first element on the queue and it’s accept state is a new undefined State.\
Different fragments are created when an operator is encountered on the queue. \
The list of operators are as follows, catenation ('.'), alternation ('|'), zero or more ('*'), zero or one ('?') and one or more ('+').\
\
Catenation: 2 fragments are taken from the queue and they are merged into a new fragment. The start state becomes fragment2’s start state and the accept state becomes fragement1’s accept state. To tie them together fragement2’s accept state becomes fragment1’s start state. \
Alternation: 2 fragments are taken from the queue. Logically, alternation means that either fragment will be accepted. So, the accept state of the new fragment must be a fragemnt1’s start state or fragement2’s start state. This is achieved by creating a new State object with edges set to an array of both start states. Accept states are not defined but an accept state must be set for each fragment. Both are new State objects.\
Zero or One: One fragment is taken from the queue and similar logic to alternation is applied except rather than set accept states as an array of 2 fragments start state, it is set as an array of 1 fragment’s start state and a new empty state object. Accept state is set as an array of 2 new State objects. \
Zero or Many: Like zero or one. If the fragment takes the path of the fragment from the queue, then it must always return to the start state of fragment to allow it to re-enter this fragment. This means that the start states are the same as above but the accept states are different, they must be an array of fragment’s start and a new State object.\
One of More: One fragment is taken from the queue. The new fragment created must have one start state and 2 accept states. The accept state must be the fragment from the queues start state and the accept state must be either the fragment from the queues start state or a new State. \
In understanding this it is helpful to be able to visualise the NFA fragments. \
\
![NFA Diagram](https://github.com/eoinwilkie/Sem6_GraphTheoryAssessment/blob/master/img/NFA_diagrams.png)


Match()\
The match function will return true if the regular expression matches the string input.\
First the regex is compiled with the compile\
\
\
## References
\
https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/index.html \
Explores the basics of automata theory, a classic automata problem, and some of the many applications of automata.\
\
https://vivadifferences.com/difference-between-dfa-and-nfa/ \
Describes both DFA’s and NFA’s and details the differences between them. \
\
https://www.cs.york.ac.uk/fp/lsa/lectures/REToC.pdf \
Provides step-by-step conversion of Regular expression’s, with images.  Also provides an implementation in the C programming language.\
\
https://people.cs.clemson.edu/~goddard/texts/theoryOfComputation/3a.pdf \
Describes Nondeterministic Finite Automata and provides examples. \
\
https://brilliant.org/wiki/shunting-yard-algorithm/  \
 Details the Shunting Yard Algorithm, providing examples.\
\
https://swtch.com/~rsc/regexp/regexp1.html \
Describes the several aspects of this project including regular expressions, finite automata, NFA’s and algorithms. The illustrations of NFA’s were particularly helpful in understanding how they work.\
\
https://www.cs.unc.edu/~plaisted/comp455/slides/nfa2.2.pdf \
Describes Nondeterministic Finite Automata and provides examples.\

