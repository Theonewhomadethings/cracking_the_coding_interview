class Node:
    def __init__(self, vertex, adjacent_length):
        self.adjacent = [None] * adjacent_length
        self.adjacentCount = 0
        self.vertex = vertex
        self.state = None

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
