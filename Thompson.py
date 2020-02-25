# author: Eoin Wilkie
# classes used in Thompson's Construction

class State:
	# Every state has 0, 1, or 2 edges from it.
	edges = []
	
	# Label for the arows. Nne means epsilon.
	label = None
	
	# Is this an accept state
	def __init__(self, label=None, edges=[]):
		self.edges = edges
		self.label = label
	
	
class Fragment:
	# Start state of the NFA fragment.
	start = None
	# Accept state of the NFA fragement.
	accept = None
	
	# Constructor
	def __init__(self, start, accept):
		self.start = start
		self.accept = accept
	
	
	
def shunt(infix):
	"""
	Shunting Yard Algorithm
	"""
	infix = "(a|b).c*"
	print("Input is " + infix)
	# Expected output: "ab|c*."
	
	# Covert input to a stack-ish list.
	infix = list(infix)[::-1]
	
	# Operator stack.
	opers = []
	# Output list.
	postfix = []
	
	# Operator List
	prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}
	
	# Loop though the input one character at a time.
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
				postfix.append(opers.push())
			opers.append(c)
		else:
			postfix.append(c)
	
	#pop all operators to the output.
	while opers:
		postfix.append(opers.pop())
	
	
	
	
	# Convert output list to string.
	return ''.join(postfix)

	
'''
myinstance = State(label="a", edges=[])
myotherintance = State(edges=[myinstance])
myFrag = Frag(myinstance, myotherintance)


print(myinstance.label)
print(myotherintance.edges[0])
print(myFrag)
'''

def regex_compile(infix):
	postfix = shunt(infix)
	postfix = list(postfix)[::-1]

	nfa_stack = []
	
	while postfix:
		# Pop a character from postfix
		c = postfix.pop()
		
		if c == '.':
			# Pop 2 fragments off the stack
			frag1 = nfa_stack.pop()
			frag2 = nfa_stack.pop()
			# Point frag2's accept start at frag1's start state
			frag2.accept.edges.append(frag1.start) 
			# Create new instance of Fragment to represent the new NFA
			newfrag = Fragment(frag2.start, frag1.accept)
			# Push the new NFA to the NFA stack
			nfa_stack.append(newfrag)
		elif c == '|':
			# Pop 2 fragments off the stack
			frag1 = nfa_stack.pop()
			frag2 = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges = [frag2.start, frag1.start])
			# Point the old accept state to the new one
			frag2.accept.edges.append(accept)
			frag1.accept.edges.append(accept)
			# Create new instance of Fragment to represent the new NFA
			newfrag = Fragment(start, accept)
			nfa_stack.append(newfrag)
		elif c == '*':
			# Do something
			frag = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges=[frag.start, accept])
			# Point the arrows
			frag.accept.edges = [frag.start, accept]
			# Create new instance of Fragment to represent the new NFA
			newfrag = Fragment(start, accept)
			nfa_stack.append(newfrag)
		else:
			accept = State()
			start = State(label=c, edges=[accept])
			# Create new instance of Fragment to represent the new NFA
			newfrag = Fragment(start, accept)
			nfa_stack.append(newfrag)
			

	
	
def match(regex, s):
	# This function will return true if and only if the regular expression
	# regex (fully) matches the string s. Returns false otherwise.
	
	# Compile the regular expression into the NFA.
	nfa = regex_compile(regex)
	# Ask the NFA if it matches the string s.
	return nfa


print(match("a.b|b*", "bbbbbbbbbbb"))

