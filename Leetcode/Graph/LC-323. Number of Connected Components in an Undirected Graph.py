
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.
#
# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
#
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the
# same as [1, 0] and thus will not appear together in edges.

# Depth First Search: O(V+E): Algorithm

#     1.Build a graph using the list of edges. Maintain a set called visited to track the nodes
#     which have been visited so far.
#     2. Iterate through all vertices and call DFS on each unvisited vertex. The DFS on that vertex
#     will mark all reachable nodes with that vertex. That constitutes a component abd we increment
#     the count for components.

class Graph:

    # DFS Recursion
    def countComponents(self,n, edges):

        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        # ---------------------------
        visited = [0] * n
        g = {x: [] for x in xrange(n)}

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # Since undirected edges

        ret = 0
        for i in xrange(n):   # We are doing for all nodes because ...( see below comment)
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1
        return ret

    # Note: Important - In regular graph DFS traverses only the vertices reachable
    # from a given source vertex. All the vertices may not be reachable from a given
    # vertex (example Disconnected graph). To do complete DFS traversal of such
    # graphs, we must call DFSUtil() for every vertex.


if __name__ == '__main__':

    g = Graph()
    vertices = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print"\n Total Connected Components: ",g.countComponents(vertices, edges)


'''

# This is simple DFS where we are iterating for all vertices and then counting components.
# If you have done Topological Sort, finding cycles.. this is same style. 

# Below also WORKS - Same as Connected Component.py - only trick is you need to add edges in both directions !

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

    def connectedComponents(self):

        visited = [False] * (len(self.graph))
        components = 0
        for node in range(0,len(self.graph)):  # [Aditya] simple DFS where we are iterating for all vertices and then counting components. Jsut like we did in Topological Sort and Finding cycle in DAG
            if visited[node] == False:
                self.DFSUtil(node, visited)
                components += 1
                print " "
        print "\nTotal Components =", components


# Driver code - Create a graph given in the above diagram

if __name__ == '__main__':

    g = Graph()

    # LC-323 : Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]] : Output = 2

    g.addEdge(0, 1)
    g.addEdge(1, 0) # Note since this is undirected so we add edges in both directions

    g.addEdge(1, 2)
    g.addEdge(2, 1) # Note since this is undirected so we add edges in both directions

    g.addEdge(3, 4)
    g.addEdge(4, 3) # Note since this is undirected so we add edges in both directions

    g.connectedComponents()
    
'''

####################################################

''''
# Iterative Solution using BFS:

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph = {i: set() for i in xrange(n)}
        
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        seen = set()
        count = 0
        
        def bfs(node):
            queue = [node]
            for n in queue:
                for nei in graph[n]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
        
        for i in range(n):
            if i not in seen:
                bfs(i)
                count += 1
        
        return count
        
'''

'''

Python Union Find:

def countComponents(self, n, edges):
    roots = range(n)
    groups = {i:{i} for i in roots}
    
    for n1, n2 in edges:
        r1, r2 = roots[n1], roots[n2]
        if r1 == r2:
            continue
        l1 = len(groups.get(r1, []))
        l2 = len(groups.get(r2, []))
        if l1 < l2:
            r1, r2 = r2, r1
        groups[r1] |= groups[r2]
        for i in groups.pop(r2, []):
            roots[i] = r1

    return len(groups)
    

'''