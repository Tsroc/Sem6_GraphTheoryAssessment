'''A Nondeterministic finite automaton (NFA) is represented as a fragement with a start state and an accept state.
'''

class State:
	"""	A state with one or two arrows, all edges labled by a label. """
	
	# Constructor.
	def __init__(self, label=None, edges=[]):
		# Every state has 0, 1, or 2 edges from it.
		self.edges = edges if edges else []
		# Label for the arows. Nne means epsilon.
		self.label = label
	
class Fragment:
	""" An NFA fragment with a start state and an accept state. """
	
	# Constructor.
	def __init__(self, start, accept):
		# Start state of the NFA fragment.
		self.start = start
		# Accept state of the NFA fragement.
		self.accept = accept