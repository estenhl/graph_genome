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

def map_global_alignment_to_graph(alignment, graph):
	curr = graph.head
	seq = []
	
	i = 0
	while (i < len(alignment)):
		while (alignment[i] == node.INDEL and i < len(alignment)):
			seq.append(None)
			i += 1

		if (i < len(alignment)):
			curr = curr.get_neighbour_by_value(alignment[i])

		seq.append(curr)
		if (not curr):
			return False

		i += 1

	return seq



