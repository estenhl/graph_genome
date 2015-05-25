from node import Node
from graph import *

completed_tests = 0
failed_tests = 0

def assert_equal(expected, received):
	global completed_tests
	global failed_tests

	completed_tests += 1
	if (expected != received):
		failed_tests += 1
		print('Mismatch in test ' + str(completed_tests))
		print('Expected:')
		print(expected)
		print('Got:')
		print(received)

	print('Failed ' + str(failed_tests) + ' out of ' + str(completed_tests) + ' total tests')

# Node unit tests
node = Node('A')
assert_equal('A', node.value)
node2 = Node('T')
node.add_neighbour(node2)
node.add_neighbour(node2)
assert_equal(1, len(node.neighbours))

# Graph unit tests
graph = Graph('test', 'ACTGGCTAGAAGCGCGCT')
assert_equal('test', graph.name)
assert_equal('ACTGGCTAGAAGCGCGCT', get_linear_sequence(graph))
print(get_all_sequences(graph))
assert_equal(1, len(get_all_sequences(graph)))
assert_equal('ACTGGCTAGAAGCGCGCT', get_all_sequences(graph)[0])

node1 = graph.head.neighbours[0]
node2 = node1.neighbours[0]
node3 = node2.neighbours[0]
node4 = node3.neighbours[0]

assert_equal('A', node1.value)
assert_equal('C', node2.value)
assert_equal('T', node3.value)
assert_equal('G', node4.value)

assert_equal([node1, node2, node3, node4], map_global_alignment_to_graph('ACTG', graph))
assert_equal([node1, node2, None, None, node3], map_global_alignment_to_graph('AC--T', graph))

graph1 = Graph('test', 'ACCT')
graph2 = Graph('test', 'ACGT')
graph3 = Graph('test', 'ACTCT')
graph4 = Graph('test', 'ACT')
merged = merge_from_alignments(graph1, graph2, 'ACCT', 'ACGT')
merged = merge_from_alignments(merged, graph3, 'AC-CT', 'ACTCT')
merged = merge_from_alignments(merged, graph4, 'ACCT', 'AC-T')
print(get_all_sequences(merged))
		