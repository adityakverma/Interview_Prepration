
# https://www.geeksforgeeks.org/topological-sorting/
# See the VIDEO <=== BEST for Quick understanding

#  Algorithm to find Topological Sorting:
#
#  For Directed Acyclic Graph (DAG), topological sort is the linear sorting of
#  vertices such that for every directed edge (u,v), vertex u comes before v
#  in ordering.

#  We can modify DFS to find Topological Sorting of a graph. In DFS, we start from
#  a vertex, we first print it and then recursively call DFS for its adjacent vertices.

#  IMP: In topological sorting, we use a temporary stack. We don't print the vertex immediately,
#  We first recursively call topological sorting for all its adjacent vertices, then push
#  it to a stack. Finally, print contents of stack. Note that a vertex is pushed to stack
#  only when all of its adjacent vertices (and their adjacent vertices and so on) are
#  already in stack.

#  APPLICATIONS:
#  Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs.
#  Determining the order of compilation tasks to perform in makefiles, data serialization, and
#  resolving symbol dependencies in linkers

# NOTE: This is same recursive DFS, additionally we are just using STACK to push results
# of topological sort.

# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #---------------------------------------------------------
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Note-1: So if we have reached to end of all neighbours, store it on stack
        # [So in video (we started with vertex A), we  first pushed 'H' because there
        # is no neighbour of H - Note its Directed Graph.]

        # Note-2: Note that a vertex is pushed to stack ONLY when all of its
        # adjacent vertices (and their adjacent vertices and so on) are already in stack.
        # [So as seen in GfG video, we had pushed 'F' before pushing 'A'. ]

        # Push current vertex to stack - which stores final sorted result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive topologicalSortUtil()
    # This is same recursive DFS we have seen. We're just doing 1.) DFS for all vertices
    # 2. passing extra stack for pushing results
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        print stack
    #---------------------------------------------------------

if __name__ == '__main__':

    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print "\nTopological Sort of the given graph:\n"
    g.topologicalSort()