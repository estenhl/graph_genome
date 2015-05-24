class Node:
	def __init__(self, value):
		self.value = value
		self.neighbours = []

	def add_neighbour(self, neighbour):
		self.neighbours.append(neighbour)