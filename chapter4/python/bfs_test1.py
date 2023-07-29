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

Repeat for DFS
'''

'''
BFS algo pseudocode
Step 1: Initially queue and visited arrays are empty

Step 2: Push node 0 into queue and mark it visited.

Step 3: Remove node 0 from the front of queue and visit the unvisited neighbours
and push them into queue

Step 4: Remove node 
'''
from collections import defaultdict


#This class represents a directed graph using adjency list representation

class directedGraph:
    #constructor
    def __init__(self):

        #default dictionary to store graph
        self.graph = defaultdict(list)

    #Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    #Function to print a BFS of a graph
    def BFS(self, s):
        #Mark all vertices as not visited
        visited = [False] * (max(self.graph)+1)

        #Create a queue for BFS
        queue = []

        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            #Dequeue a vertex from a queue and print it
            s = queue.pop(0)
            print(s, end = " ")
            '''
            Get all adjacent vertices of the dequeued vertex s. If an adjacent 
            has not been visited, then mark it visited and enqueue it.
            '''
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    #create a graph given in the above diagram
    g = directedGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("  Breadth first traversal starting from vertex 2")
    g.BFS(2)