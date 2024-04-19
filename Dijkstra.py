from queue import PriorityQueue
import heapq


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.marked = False

    def add_neighbor(self, node, distance=1):
        self.neighbors.append((node, distance))

    def mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked


class Dijkstra:
    """
    Expects a list of nodes and a distance threshold.
    """
    def __init__(self, nodes: Node):
        self.nodes = nodes
        self.run = PriorityQueue

    def find_distance(self, start_node: Node, end_node: Node):
