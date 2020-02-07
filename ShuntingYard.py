#! /usr/bin/env python3

# Eoin Wilkie
# Shunting Yard Algorithm

def runFunction():
	"""
	Shunting Yard Algorithm
	"""
	#str = "2+5*4"
	#operatorList = ["+", "-", "*", "/"]
	str = "W.h.a.l.e.a*"
	operatorList = [".", "|", "*"];
	
	tokenList = []
	operatorStack = []
	outputQueue = []
	
	# add str to tokenList
	'''
	for char in str:
		tokenList.append(char)
	#test tokenList
	'''
	'''
	for token in tokenList:
		print(token)
	'''
	#add token to operatorStack & outputQueue
	for token in str:
		if token in operatorList:
			operatorStack.append(token)
		else:
			outputQueue.append(token)
	
	#print operatorStack
	'''
	print("Operator Stack:")
	for token in operatorStack:
		print(token)
	
	print("Output Queue:")
	for token in outputQueue:
		print(token)
	'''
		
	for i in range(0,len(operatorStack)):
		outputQueue.append(operatorStack.pop())
	
	print("New Output Queue")
	for token in outputQueue:
		print(token)
	
	
	
	
runFunction()

