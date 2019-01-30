
# Python program to print DFS traversal from a given given graph
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

    # ----------------- ITERATIVE -----------------------------------

    def DFS_Iterative(self, source):

        stack = []
        stack.append(source)  # We append first so looks like PreOrder DFS - similar to tree.

        dist = defaultdict(list)
        dist[source] = 0

        while stack:
            node = stack.pop()
            print node,  # OR result.append(node)

            for neighbour in self.graph[node]:
                if neighbour not in dist:
                    dist[neighbour] = dist[node] + 1
                    stack.append(neighbour)

        print "\nDistance map is ", (dist.items())  # Additional Info

    # ----------------- RECURSIVE -----------------------------------
    # A function used by DFS
    def DFSUtil(self, node, dist):
        print node,
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[node]:
            if neighbour not in dist.keys():
                dist[neighbour] = dist[node] + 1  # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
                self.DFSUtil(neighbour, dist)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS_Recursive(self ,source):
        dist = defaultdict(list) # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
        dist[source]=0           # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(source, dist)

        print "\nDistance map",\
        dist.items()

    # ---------------------------------------------------------------

if __name__ == '__main__':

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(1, 4)

    print "\nRecursive DFS from (starting from vertex 2): ",
    g.DFS_Recursive(2)

    print "\nIterative DFS from (starting from vertex 2): ",
    g.DFS_Iterative(2)

