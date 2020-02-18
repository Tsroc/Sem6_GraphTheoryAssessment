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
	
myinstance = State(label="a", edges=[])
myotherintance = State(edges=[myinstance])
print(myinstance.label)
print(myotherintance.edges[0])