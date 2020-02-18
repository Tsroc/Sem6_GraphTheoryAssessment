#! /usr/bin/env python3

# Eoin Wilkie
# Shunting Yard Algorithm

def runFunction():
	"""
	Shunting Yard Algorithm
	"""
	# Operator List
	prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}
	
	# The input
	infix = "(a|b).c*"
	print("Input is " + infix)
	# Expected output: "ab|c*."
	
	# Covert input to a stack-ish list.
	infix = list(infix)[::-1]
	
	# Operator stack.
	opers = []
	# Output list.
	postfix = []
	
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
	postfix = ''.join(postfix)
	
	# Print the result.
	print("Output is " +postfix)
	
runFunction()