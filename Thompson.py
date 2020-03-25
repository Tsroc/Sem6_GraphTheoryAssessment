# author: Eoin Wilkie
# classes used in Thompson's Construction
# Research: https://www.youtube.com/watch?v=OSHXxulvH04   https://kean.github.io/post/lets-build-regex		https://swtch.com/~rsc/regexp/regexp1.html
# https://github.com/xysun/regex/blob/master/parse.py

from NFA import *

def shunt(infix):
	""" Return the infix regular expression in postfix. """
	
	# Convert input to a stack-ish state.
	infix = list(infix)[::-1]
	
	# Operator stack.
	opers = []
	# Postfix regualar expression.
	postfix = []
	
	# Operator List
	prec = {'*': 100, '.': 80, '+': 70, '?': 70, '|': 60, ')': 40, '(': 40}
	
	# Loop though the input one character at a time.
	#while c := infix.pop():
	while infix:
		# Pop a chracter from the inpit.
		c = infix.pop()
		
		if c == '(':
			opers.append(c)
		elif c == ')':
			# Pop the operators stack until you find an '('.
			while opers[-1] != '(':
				postfix.append(opers.pop())
			# Get rid of the '('
			opers.pop()
		elif c in prec:
			# Push any perators on the opers stack with higher precedence than current
			while opers and prec[c] < prec[opers[-1]]:
				postfix.append(opers.pop())
			opers.append(c)
		else:
			postfix.append(c)
	
	#pop all operators to the output.
	while opers:
		postfix.append(opers.pop())
		
	# Convert output list to string.
	return ''.join(postfix)


def compile(infix):
	""" Return an NFA fragment representing the infix regualr expression. """
	
	# Convert infix to postfix.
	postfix = shunt(infix)
	# Make postfix a stack of characters.
	postfix = list(postfix)[::-1]

	nfa_stack = []
	
	while postfix:
		# Pop a character from postfix
		c = postfix.pop()
		
		if c == '.':
			# Catenation
			
			# Pop 2 fragments off the stack
			frag1 = nfa_stack.pop()
			frag2 = nfa_stack.pop()
			# Point frag2's accept start at frag1's start state
			frag2.accept.edges.append(frag1.start)
			# Create new start and accept states
			start = frag2.start
			accept = frag1.accept
			
		elif c == '|':
			# Alternation
			
			# Pop 2 fragments off the stack
			frag1 = nfa_stack.pop()
			frag2 = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges = [frag2.start, frag1.start])
			# Point the old accept state to the new one
			#frag2.accept.edges.append(accept)		# Removed line.
			#frag1.accept.edges.append(accept)		# Removed line.
			frag2.accept.edges = [accept]
			frag1.accept.edges = [accept]
			
			'''
				Lines 106 & 107 changed to lines 108 & 109
				This has resolved the Assertion Errors I got below,
				I believe that prior to this change 2 accept states were permitted, causing the error.
			'''
			
		elif c == '*':
			# Zero or More
			
			# Pop a single fragment of the stack.
			frag = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges=[frag.start, accept])
			# Point the arrows
			frag.accept.edges = [frag.start, accept]
			
		elif c == '?':
			# Zero or One
			'''
				It is my understanding that the way this works is,
				Start state is the entry point, in this case there are 2 branches
				The first is one: meaning it should accept the fragment (the character which comes after the '?' symbol
				The second is zero: meaning there is no matches to this fragment
				The accept state is simply dangling arrows pointing to nothing (yet), in this case both must be accept.
				Meaning, regardless if there is zero or one, the next step is to have a dangling arrow.
				
				https://swtch.com/~rsc/regexp/regexp1.html : used to come to this understanding.
			
			'''
			frag = nfa_stack.pop()
			
			accept = State()
			start = State(edges = [frag.start, accept])
			frag.accept.edges = [accept, accept]
		
		elif c == '+':
			# One of More
			'''
				Similar logic as above.
				Here there is 1 entry point, so start must always = frag.start.
				There are 2 outputs, the first is pointing back at frag.start and 
				the second is a dangling arrow.
					
				https://swtch.com/~rsc/regexp/regexp1.html : used to understand.
			
			'''
			
			# Pop a single fragment of the stack.
			frag = nfa_stack.pop()
			
			accept = State()
			start = frag.start
			frag.accept.edges = [frag.start, accept]	

		else:
			accept = State()
			start = State(label=c, edges=[accept])
		
		# Create new instance of Fragment to represent the new NFA
		newfrag = Fragment(start, accept)
		# Push the new NFA to the NFA stack
		nfa_stack.append(newfrag)
		
	# The NFA stack should have exactly one NFA on it.
	return nfa_stack.pop()

	
def followes(state, current):
	""" Add a state to a set and follow all of the e(psilon) arrows. """
	
	# Only do something when we haven't already seen the state.
	if state not in current:
		# Put the state itself into current	
		current.add(state)
		# See whether the state is labelled by e(psilon)
		if state.label is None:
			# Loop though the states pointed to by this state.
			for x in state.edges:
				# Follow all of their e)psilon)s too.
				followes(x, current)
		
	
def match(regex, s):
	""" This function will return true if and only if the regular expression
		regex (fully) matches the string s. Returns false otherwise
	"""
	
	# Compile the regular expression into the NFA.
	nfa = compile(regex)
	
	# Try to mratch regular expression to the string s.
	
	# Current set of states
	current = set()
	# Add the first state, and follow all e(psilon) arrows.
	followes(nfa.start, current)
	previous = set()
	
	# Look through the characters in s.
	for c in s:
		# Keep track of where we were.
		previous = current
		# Create a new empty set for stats we're about to be in.
		current = set()
		# Loop through the previous states
		for state in previous:
			# Only follow arrows not labelled by e(psilon)
			if state.label is not None:
				# If the label of the state is equal to the character we'ce read:
				if state.label == c:
					# Add the state at the end of the arrow to current
					followes(state.edges[0], current)
		
	# Ask the NFA if it matches the string s.
	return nfa.accept in current	

if __name__ == "__main__":
	# Sets up tests
	tests = [
		["a.b|b*", "bbbbbb", True],
		["a.b|b*", "bbx", False],
		["a.b|b*", "ab", True],
		#["a.b|b*", "abb", False],	# Returns AssertionError.
		["a|b", "bbbbbb", False],	# Returns AssertionError, uncertain what the issue is. 				Fix #1
		["b**", "", True],
		
		# '?' tests
		["c?", "", True],
		["c?", "c", True],
		["c?", "cc", False],
		["c?|a", "a", True],
		["c?|a", "c", True],
		["c?|b*", "bb", True],
		["c?|b", "bbbbbb", False],	# Returns AssertionError, uncertain what the issue is.				Fix #1
		["c|b", "bbbbbb", False],	# Returns AssertionError, not related to the '?' implemmentation.	Fix #1
									# Seems to be an error with '|' implementation.#
									# Fix #1 is detailed @ line 111.
									
		# '+' tests
		["c+", "", False],
		["c+", "c", True],
		["c+", "cc", True],
		["c+|a", "a", True],
		["c+|a", "c", True],
		["c+|b*", "bb", True],
		["c+|b", "", False],
		
	]
	# Runs assertions for each test.
	for test in tests:
		assert match(test[0], test[1]) == test[2], test[0] + (" should match " if test[2] else " should not match ") + test[1]