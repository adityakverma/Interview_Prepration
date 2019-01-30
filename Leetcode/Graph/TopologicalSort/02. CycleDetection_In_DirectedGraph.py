
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

# Depth First Traversal can be used to detect a cycle in a Graph. There is a cycle
# in a graph only if there is a back edge present in the graph

# To detect cycle, we can check for cycle in individual trees by checking back edges.
# To detect a back edge, we can keep track of vertices currently in recursion stack of
# function for DFS traversal. If we reach a vertex that is already in the recursion stack,
# then there is a cycle in the tree.

# Python program to detect cycle in a graph
#  [Aditya]: This is a RECURSIVE DFS Traversal. Similar to Topological Sort.

from collections import defaultdict

class Graph():

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v) # Just one side, since its directed graph.

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours if any neighbour is visited and in recStack
        # then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True: # Now if node is present in recStack, that means Cycle is present.
                return True # Meaning Cycle is present.

        recStack[v] = False # The node needs to be poped from recursion stack before function ends
        return False  # Else cycle is not Present.

    # This is same recursive DFS we have seen. We're just doing 1.) DFS for all vertices
    # 2. passing extra stack (recStack) for flagging vertices which are already visited (back edges).
    # Returns true if graph is cyclic else false
    def isCyclic(self):

        visited = [False] * self.V
        recStack = [False] * self.V

        for node in range(self.V):  # DFS for all vertices -Just like Topological Sort
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

if __name__ == '__main__':

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    if g.isCyclic() == 1:
        print "\nGraph has a cycle"
    else:
        print "\nGraph has no cycle"