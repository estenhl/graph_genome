import node

class Graph:
	def __init__(self, name, sequence):
		self.name = name
		self.head = node.Node('<s>')
		prev = self.head
		for char in sequence:
			curr = node.Node(char)
			prev.add_neighbour(curr)
			prev = curr

		curr = node.Node('<e>')
		prev.add_neighbour(curr)

def get_linear_sequence(graph):
	curr = graph.head.neighbours[0]
	sequence = ''

	while(not curr.value == '<e>'):
		sequence += curr.value
		curr = curr.neighbours[0]

	return sequence