'''
Problem 4.1 : Route Between Nodes
_________________________________
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Hints:
127 - Two well-known algorithms can do this. What are the tradeoffs between them?

'''

'''
I am trying to implement breadth first search and depth first search to see if there is a route between two nodes 

Simple graph traversal.
We start with one of the two nodes and during traversal, check if the other node is found. We should
mark any node found in the coure of the algorithm a already visited to avoid cycles and reptition of the nodes

Steps for me to solve:
Start with BFS
BFS is implemented with a queue data structure in an iterative manner.
So first build the queue back end in a different file in a Linked list implementation
Once the queue is built then work on building the BFS algorithm
BFS algorithm:
- Choose the datastructure for the seen values hashset
- Add start to the search
- Pull a node
-process if not seen
- add unseen children nodes
after general BFS algo is built then make any adjustments to solve the answer directly.
'''

import unittest
from collections import deque

# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R

'''
Depth first search is_route function
This function traverses the graph, starting from the start node and checks
if there is a route to the end node. It maintains a visited set to keep track
of the nodes it has already visited to avoid cycles.
'''
def is_route(graph, start, end, visited = None):
    #If the visited set is not provided, initialize it as an empty set 
    if visited is None:
        visited = set()

    #Iterate over each node adjacent to the start node in the graph
    for node in graph[start]:
        #Check if the node has not been visited before 
        if node not in visited:
            #Add the node to the visited set to mark it as visited
            visited.add(node)
            '''
            Check if the current node is the target end node or recursively call
            the function with the current node as the new start node to explore its 
            adjacent nodes.
            '''
            if node == end or is_route(graph, node, end, visited):
                #Or if a route is found, return True
                return True
    '''
    If no route is found after exploring all adjacent nodes, return False indicating
    there is no route from start to end,
    '''
    return False


'''
Bread first search approach to traverse the graph.
Starts from the start node and checks if there is a route to the end node.
It mantains a visited set to keep track of the visited nodes and uses a queue
to explore the graph in a breadth-first manner. If it encoutners the end node 
during the traversal, it returns True. Otherwise it returns False. 

'''
def is_route_BFS(graph, start, end):
    #Check if the start and end nodes are the same
    if start == end:
        return True
    
    #Initialize an empty set to keep track of visited nodes
    visited = set()
    #Create a queue using deque to perform breadth first search (BFS)
    queue = deque()
    queue.append(start)

    #Perform BFS until the queue is empty
    while queue:
        #Get the next node from the front of queue
        node = queue.popleft()
        #Iterate over each adjacent node of the current node in the graph
        for adjacent in graph[node]:
            #Chec if the adjacent node has not been visited before
            if adjacent not in visited:
                #Check if the adjacent node is the target end node
                if adjacent == end:
                    return True
                else:
                    #Add the adjacent node to the queue for further exploration
                    queue.append(adjacent)

        #Mark the current node as visited
        visited.add(node)
    #If no route is found after exploring all nodes, return False
    return False



class Test(unittest.TestCase):
    
    '''
    Graph representation, where each key represents a node in the graph and the 
    corresponding value is a list of its adjacent nodes

    This representation allows you to easily access the adjacent nodes of a particular node 
    by using the node name as the key in the dictionary. It provides a concise and efficient 
    way to represent the connectivity of nodes in a graph.
    '''
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        #Iterate over each test case in the test lists
        for [start, end, expected] in self.tests:
            #Call the is route function with the given start and end nodes
            actual = is_route(self.graph, start, end)
            #Check if the actual result matches the expected result
            assert actual == expected

    def test_is_route_BFS(self):
        #Iterate over each test case in the tests list
        for [start, end, expected] in self.tests:
            #Call the is route BFS function with the given start and end nodes
            actual = is_route_BFS(self.graph, start, end)
            #check if the actual result matches the expected result
            assert actual == expected
        
if __name__ == "__main__":
    unittest.main()