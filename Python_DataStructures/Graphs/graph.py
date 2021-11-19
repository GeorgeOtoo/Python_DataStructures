# A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

#create a graph class
class Graph:

    #create a constructor to initialize when the class is called
    def __init__(self):
        self.graphing = {}
    

    #create a method to create a vertex and add to the graph
    def add_vertex(self, vertex):
        if vertex not in self.graphing:
            self.graphing[vertex] = [] #adds your vertex to the graph and assigns an empty list
            return True
        return False

    #create a method to add the edges 
    def add_edge(self, vertex1, vertex2):

        #check if either vertecies exist in the graph
        if vertex1 in self.graphing.keys() and vertex2 in self.graphing.keys(): 
            self.graphing[vertex1].append(vertex2) #add them to each list
            self.graphing[vertex2].append(vertex1)

            return True
        return False

    
    #remove the edge 
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graphing.keys() and vertex2 in self.graphing.keys(): #if it exists in the graph
            try:
                self.graphing[vertex1].remove(vertex2) #delete vertex 2 in the list of vertex 1
                self.graphing[vertex2].remove(vertex1) #delete vertex 1 in the list of vertex 2
                return True
            except ValueError:
                pass
        return False


    #remove vertex
    def remove_vertex(self, vertex):
        if vertex in self.graphing.keys(): #if the vertex exist in the graph
            for i in self.graphing[vertex]: #loop through the value of the vertex
                self.graphing[i].remove(vertex) #go to the key and remove the vertex from the list
                #self.graphing[vertex].remove(vertex)
            del self.graphing[vertex]
            return True
        return False




    #print function to loop through the graph
    def print_graph(self):
        for vertex in self.graphing:
            print(vertex, ":", self.graphing[vertex])


#create your graph
my_graph = Graph()

#add vertices
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("F")

#add edges
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("F", "B")
my_graph.add_edge("C", "F")
my_graph.add_edge("D", "F")
my_graph.add_edge("A", "F")


#remove edges
#my_graph.remove_edge("A", "C")
#my_graph.remove_edge("D", "F")


#remove vertex
my_graph.remove_vertex("F")

#print graph"
my_graph.print_graph()