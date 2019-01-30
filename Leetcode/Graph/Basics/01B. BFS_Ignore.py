# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# Breadth First Traversal (or Search) for a graph is similar to Breadth First
# Traversal of a tree (See method 2 of this post). The only catch here is,
# unlike trees, graphs may contain cycles, so we may come to the same node again.
# To avoid processing a node more than once, we use a boolean visited array.

# Program to print BFS traversal from a given source
# vertex. BFS(int s) traverses vertices reachable from s.

# [ADITYA] : THIS IS BFS ALGORITHM DOING VIA ITERATIVE METHOD USING QUEUE.
#  WE CAN ALSO DO THIS BY RECURSION

############################  IMPORTANT ##########################################

# [ADITYA]: ITERATIVE METHOD FOR BFS AND DFS ARE EXACTLY SAME IN GRAPH- EXCEPT USE
# OF STACK IN DFS (and stack.pop()) AND USE OF QUEUE IN BFS ALGO ( AND queue.pop(0)
# OR queue.popleft() IF WE USED collections.deque

# BFS pseudocode
#
# create a queue Q
# mark v as visited and put v into Q
# while Q is non-empty
#     remove the head u of Q
#     mark and enqueue all (unvisited) neighbours of u

##################################################################################

from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, src):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []
        queue.append(src) # We append first so looke like PreOrder DFS - similar to tree.

        visited[src] = True

        while queue:
            node = queue.pop(0)  # Or if we've used collections.deque then we would have done queue.popleft()
            print node, # OR result.append(node)

            for neighbour in self.graph[node]:
                if visited[neighbour] == False:
                    queue.append(neighbour)    # Note: In this case (BFS), we keep appending all unvisited neighbours to queue, where as in DFS we go into depth (next level) by calling recursion.
                    visited[neighbour] = True

    '''
    # For Reference: LC-133, Graph Clone we applied this BFS
    
    class UndirectedGraphNode:
    
        def __init__(self, x):
            self.label = x
            self.neighbors = []
    
        def cloneGraph1(self, node):
            if not node:
                return 
                
            nodeCopy = UndirectedGraphNode(node.label)  # Extra : Creating node copy for clone graph
            dic = {node: nodeCopy}                      # Extra : Creating map for clone graph
            queue = collections.deque([node])
            
            while queue:
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor not in dic: # neighbor is not visited
                    
                        neighborCopy = UndirectedGraphNode(neighbor.label)  # Extra : Creating neighbour copy for clone graph
                        dic[neighbor] = neighborCopy                        # Extra : Filling up for clone
                        dic[node].neighbors.append(neighborCopy)            # Extra : Appending neighbour of clone
                        
                        queue.append(neighbor)
                    else:
                        dic[node].neighbors.append(dic[neighbor])
            return nodeCopy
    '''

# Driver code Create a graph given in the above diagram

if __name__ == '__main__':

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    #g.addEdge(1, 4)



    print "\nFollowing is BFS (starting from vertex 2)"
    g.BFS(2)


#########################################################################################

'''
from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)   # Container datatypes 1

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS_aditya(self, source):

        queue = []
        queue.append(source)

        dist = defaultdict(list)
        dist[source] = 0

        while queue:
            node = queue.pop(0)
            print node,

            for neighbour in self.graph[node]:
                if neighbour not in dist.keys():
                    dist[neighbour] = dist[node] +1
                    queue.append(neighbour)

        print "\nDistance map is ",(dist.items()) # Additional Info

# Driver code
# Create a graph given in the above diagram
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 0)
g1.addEdge(2, 3)
g1.addEdge(3, 3)

g2 = Graph()
g2.addEdge('a', 'c')
g2.addEdge('b', 'd')
g2.addEdge('c', 'e')
g2.addEdge('d', 'a')
g2.addEdge('d', 'd')
g2.addEdge('e', 'b')
g2.addEdge('e', 'c')

# graph = {
#     'a': ['c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['a', 'd'],
#     'e': ['b', 'c']
# }

print "\n\nFollowing is BFS (starting from vertex 2) is ",
print g1.BFS_aditya(2)

print "\n\nFollowing is BFS (starting from vertex d) is ",
g2.BFS_aditya('d')

print "\n\nNOTE: this is correct, because this is Directed graph"

'''