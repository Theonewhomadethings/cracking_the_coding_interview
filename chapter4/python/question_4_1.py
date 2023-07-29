from enum import Enum
from collections import deque

class State(Enum):
    Unvisited = 0
    Visited = 1
    Visiting = 2

class Node:
    def __init__(self, vertex, adjacent_length):
        self.adjacent = [None] * adjacent_length
        self.adjacentCount = 0
        self.vertex = vertex
        self.state = State.Unvisited

    def add_adjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("No more adjacent can be added")

    def get_adjacent(self):
        return self.adjacent

    def get_vertex(self):
        return self.vertex

class Graph:
    def __init__(self):
        self.vertices = []

    def add_node(self, x):
        self.vertices.append(x)

    def get_nodes(self):
        return self.vertices

def create_new_graph():
    g = Graph()
    temp = [None] * 6

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[2])
    temp[0].add_adjacent(temp[3])
    temp[3].add_adjacent(temp[4])
    temp[4].add_adjacent(temp[5])

    for i in range(6):
        g.add_node(temp[i])

    return g

def search(g, start, end):
    q = deque()
    for u in g.get_nodes():
        u.state = State.Unvisited
    start.state = State.Visiting
    q.append(start)
    while q:
        u = q.popleft()
        if u is not None:
            for v in u.get_adjacent():
                if v.state == State.Unvisited:
                    if v == end:
                        return True
                    else:
                        v.state = State.Visiting
                        q.append(v)
            u.state = State.Visited
    return False

