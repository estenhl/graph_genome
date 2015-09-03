import node

class Graph:
	def __init__(self, name, sequence):
		self.name = name
		self.head = node.Node('<s>')
		self.tail = node.Node('<e>')
		prev = self.head
		for char in sequence:
			curr = node.Node(char)
			prev.add_neighbour(curr)
			prev = curr

		prev.add_neighbour(self.tail)

def get_linear_sequence(graph):
	curr = graph.head.neighbours[0]
	sequence = ''

	while(not curr.value == '<e>'):
		sequence += curr.value
		curr = curr.neighbours[0]

	return sequence

def get_all_sequences(graph):
	def get_all_sequences_rec(node, s, paths):
		if (node.value == '<e>'):
			paths.append(s)
			return paths
		else:
			for neighbour in node.neighbours:
				get_all_sequences_rec(neighbour, s + node.value, paths)

	paths = []
	for neighbour in graph.head.neighbours:
		get_all_sequences_rec(neighbour, '', paths)

	return paths

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

def merge_from_alignments(graph1, graph2, alignment1, alignment2):
	seq1 = map_global_alignment_to_graph(alignment1, graph1)
	seq2 = map_global_alignment_to_graph(alignment2, graph2)

	if (not seq1):
		print('Unable to merge from invalid alignment 1')
		return graph1

	if (not seq2):
		print('Unable to merge from invalid alignment 2')
		return graph1

	if (len(seq1) != len(seq2)):
		print('Only able to merge global alignments with equal length')
		return graph1

	prev = [graph1.head, graph1.head]

	i = 0
	while (i < len(seq1)):
		if (seq1[i] and seq2[i] and seq1[i].value == seq2[i].value):
			merged = merge_nodes(prev, seq1[i], seq2[i])
			prev[0] = merged
			prev[1] = merged
		else:
			if (seq1[i]):
				prev[0] = seq1[i]

			if (seq2[i]):
				prev[1] = seq2[i]

		i += 1

	prev[1].neighbours = []
	prev[1].add_neighbour(graph1.tail)

	return graph1

def merge_nodes(prev, original, copy):
	for neighbour in copy.neighbours:
		original.add_neighbour(neighbour)

	if prev[0]:
		prev[0].delete_neighbour(copy)
		prev[0].add_neighbour(original)
	if prev[1]:
		prev[1].delete_neighbour(copy)
		prev[1].add_neighbour(original)

	return original


