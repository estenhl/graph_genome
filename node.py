INDEL = '-'

class Node:
	def __init__(self, value):
		self.value = value
		self.neighbours = []

	def add_neighbour(self, neighbour):
		if (not neighbour in self.neighbours):
			self.neighbours.append(neighbour)

	def get_neighbour_by_value(self, value):
		for neighbour in self.neighbours:
			if (neighbour.value == value):
				return neighbour

		return False