class directedGraph:
    def __init__(self):
        #Initialize an empty dictionary to store the graph
        self.graph = {}

    def add_vertex(self, vertex):
        #Add a new vertex to the graph
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        #Add a directed edge between 2 vertices 
        if start_vertex in self.graph and end_vertex in self.graph:
            #Append the end vertex in the adjency list of the start vertex
            self.graph[start_vertex].append(end_vertex)
        else:
            raise ValueError("One or both vertices do not exist in the graph")
        
    def remove_vertex(self, vertex):
        #Remove a vertex from the graph
        if vertex in self.graph:
            #Delete the vertex from the graph dictionary
            del self.graph[vertex]
            #Remove the vertex from all adjaency lists
            for adj_list in self.graph.values():
                if vertex in adj_list:
                    adj_list.remove(vertex)
        
        else:
            raise ValueError("Vertex does not exist in the graph. ")
        
    def remove_edge(self, start_vertex, end_vertex):
        #remove a directed edge between 2 vertices
        if start_vertex in self.graph and end_vertex in self.graph:
            if end_vertex in self.graph[start_vertex]:
            #Remove the end vertex from the adjency list of the start vertex
                self.graph[start_vertex].remove(end_vertex)
            else:
                raise ValueError("Edge does not exist between the vertices")
        else:
            raise ValueError("One or both vertices do not exist in the graph")
    
    def get_vertices(self):
        #Get a list of all vertices in the graph
        return list(self.graph.keys())

    def get_edges(self): # might need to add paramaters here
        #Get a list of all edges in the graph as tuples of start and end vertices 
        edges = [] 
        for start_vertex, adj_list in self.graph.items():
            for end_vertex in adj_list:
                edges.append((start_vertex, end_vertex))
        return edges
    
    def get_adjacent_vertices(self, vertex):
        #Get a list of adjacent vertices for a given vertex
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            raise ValueError("Vertex does not exist in the graph.")
        


class Graph:
    MAX_VERTICES = 6

    def __init__(self):
        self.vertices = [None] * self.MAX_VERTICES
        self.count = 0

    def add_node(self, x):
        if self.count < len(self.vertices):
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("Graph full")

    def get_nodes(self):
        return self.vertices

# Create a new directed graph
graph = directedGraph()

# Add vertices and edges
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')

# Get vertices and edges
print(graph.get_vertices())  # Output: ['A', 'B', 'C']
print(graph.get_edges())  # Output: [('A', 'B'), ('A', 'C')]

# Get adjacent vertices
print(graph.get_adjacent_vertices('A'))  # Output: ['B', 'C']

