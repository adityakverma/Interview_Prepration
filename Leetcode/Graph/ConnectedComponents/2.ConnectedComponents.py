
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print v,

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Note: Important - In regular graph DFS traverses only the vertices reachable
    # from a given source vertex. All the vertices may not be reachable from a given
    # vertex (example Disconnected graph). To do complete DFS traversal of such
    # graphs, we must call DFSUtil() for every vertex.

    def connectedComponents(self):

        visited = [False] * (len(self.graph))
        components = 0
        for node in range(0,len(self.graph)):  # <=== We do for all nodes as explained before and count components.
            if visited[node] == False:
                self.DFSUtil(node, visited)
                components += 1
                print " "
        print "\nTotal Components =", components


# Driver code
# Create a graph given in the above diagram

if __name__ == '__main__':

    g = Graph()
    '''
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 3)
    '''

    # LC-323 : Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]] : Output = 2

    g.addEdge(0, 1)
    g.addEdge(1, 0) # Note since this is undirected so we add edges in both directions

    g.addEdge(1, 2)
    g.addEdge(2, 1) # Note since this is undirected so we add edges in both directions

    g.addEdge(3, 4)
    g.addEdge(4, 3) # Note since this is undirected so we add edges in both directions


    g.connectedComponents()

