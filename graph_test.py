from node import Node
from graph import Graph, get_linear_sequence

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

# Graph unit tests
graph = Graph('test', 'ACTGGCTAGAAGCGCGCT')
assert_equal('test', graph.name)
assert_equal('ACTGGCTAGAAGCGCGCT', get_linear_sequence(graph))
		