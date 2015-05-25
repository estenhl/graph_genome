from node import Node
from graph import Graph
from graphics import *

SPACING = 30
RADIUS = 10
WIDTH = 1100
HEIGHT = 700
START_X = 50
START_Y = HEIGHT / 2

def draw_graph(graph):
	win = GraphWin(graph.name, WIDTH, HEIGHT)
	draw_graph_rec(win, graph.head, START_X, START_Y)
	win.getMouse()

def draw_graph_rec(win, curr, x, y):
	draw_node(win, curr, x, y)
	i = 0
	for neighbour in curr.neighbours:
		draw_graph_rec(win, neighbour, x + SPACING, y + (SPACING * i))
		draw_edge(win, x, y, x + SPACING, y + (SPACING * i))
		i += 1

def draw_node(win, node, x, y):
	pt = Point(x, y)
	circle = Circle(pt, RADIUS)
	circle.draw(win)
	text = Text(pt, node.value)
	text.draw(win)

def draw_edge(win, start_x, start_y, end_x, end_y):
	edge = Line(Point(start_x + RADIUS, start_y), Point(end_x - RADIUS, end_y))
	edge.draw(win)

if __name__ == '__main__':
	graph = Graph('Test', 'ACTGGTCATTAGGGATC')
	node2 = Node('T')
	graph.head.neighbours[0].add_neighbour(node2)
	node2.add_neighbour(graph.head.neighbours[0].neighbours[0].neighbours[0])
	draw_graph(graph)