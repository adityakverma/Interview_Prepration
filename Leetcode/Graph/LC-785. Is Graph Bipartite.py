
# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets
# A and B such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge
# between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There
# are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any
# element twice.
#
# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]: # Output: true
# Explanation: The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
#
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]] : Output: false
# Explanation: # The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.

# Note:
#     graph will have length in range [1, 100].
#     graph[i] will contain integers in range [0, graph.length - 1].
#     graph[i] will not contain i or duplicate values.
#     The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

# ------------------------------------------------------------------------------------------
# THEORY:
# bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint and independent
# sets U and V V such that every edge connects a vertex in U

# Bipartite graphs may be characterized in several different ways:
    # A graph is bipartite if and only if it does not contain an odd cycle.[14]
    # A graph is bipartite if and only if it is 2-colorable

# [Aditya] : My idea - check if there is cycle in undirected graph. If cycle present, then we
# cannot Bi-partite. Not sure if that will work. anyways let's tey below color concept
#------------------------------------------------------------------------------------------

# Approach #1: Coloring by Depth-First Search [Accepted] OR Coloring by BFS (use queue)
# a colored node should have ALL connected neighbors in different colors.

# Color a node blue if it is part of the first set, else red. We should be able to greedily
# color the graph if and only if it is bipartite: one node being blue implies all it's neighbors
# are red, all those neighbors are blue, and so on.
# For each uncolored node, we'll start the coloring process by doing a depth-first-search on
# that node. Every neighbor gets colored the opposite color from the current node. If we find
# a neighbor colored the same color as the current node, then our coloring was impossible.
# To perform the depth-first search, we use a stack. For each uncolored neighbor in graph[node],
# we'll color it and add it to our stack, which acts as a sort of todo list of nodes to visit
# next. Our larger loop for start... ensures that we color every node.
# We should be careful to consider disconnected components of the graph, by searching each node.

class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in xrange(len(graph)):
            if node not in color:

                # Iterative DFS Starts from here ...
                stack = [node]  # If using Iterative BFS, just use queue : q = collections.deque([i])
                color[node] = 0
                while stack:
                    node = stack.pop()  # If using Iterative BFS, just pop from front: q.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

if __name__ == '__main__':

    g = Solution()
    graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]
               ]

    print "Yes" if g.isBipartite(graph) else "No"

# Time Complexity: O(N+E), where N is the number of nodes in the graph, and E is the number of edges.
# We explore each node once when we transform it from uncolored to colored, traversing all its edges
# in the process.
# Space Complexity: O(N), the space used to store the color.


'''
https://www.geeksforgeeks.org/bipartite-graph/

# Python program to find out whether a  
# given graph is Bipartite or not 
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] \ 
                                for row in range(V)] 
  
    # This function returns true if graph G[V][V]  
    # is Bipartite, else false 
    def isBipartite(self, src): 
  
        # Create a color array to store colors  
        # assigned to all veritces. Vertex 
        # number is used as index in this array.  
        # The value '-1' of  colorArr[i] is used to  
        # indicate that no color is assigned to  
        # vertex 'i'. The value 1 is used to indicate  
        # first color is assigned and value 0 
        # indicates second color is assigned. 
        colorArr = [-1] * self.V 
  
        # Assign first color to source 
        colorArr[src] = 1
  
        # Create a queue (FIFO) of vertex numbers and  
        # enqueue source vertex for BFS traversal 
        queue = [] 
        queue.append(src) 
  
        # Run while there are vertices in queue  
        # (Similar to BFS) 
        while queue: 
  
            u = queue.pop() 
  
            # Return false if there is a self-loop 
            if self.graph[u][u] == 1: 
                return False; 
  
            for v in range(self.V): 
  
                # An edge from u to v exists and destination  
                # v is not colored 
                if self.graph[u][v] == 1 and colorArr[v] == -1: 
  
                    # Assign alternate color to this  
                    # adjacent v of u 
                    colorArr[v] = 1 - colorArr[u] 
                    queue.append(v) 
  
                # An edge from u to v exists and destination  
                # v is colored with same color as u 
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]: 
                    return False
  
        # If we reach here, then all adjacent  
        # vertices can be colored with alternate  
        # color 
        return True
  
# Driver program to test above function 
g = Graph(4) 
g.graph = [[0, 1, 0, 1], 
            [1, 0, 1, 0], 
            [0, 1, 0, 1], 
            [1, 0, 1, 0] 
            ] 
              
print "Yes" if g.isBipartite(0) else "No"

'''

'''
Examples

When modelling relations between two different classes of objects, bipartite graphs very often arise naturally. For instance, a graph of football players and clubs, with an edge between a player and a club if the player has played for that club, is a natural example of an affiliation network, a type of bipartite graph used in social network analysis.[6]

Another example where bipartite graphs appear naturally is in the (NP-complete) railway optimization problem, in which the input is a schedule of trains and their stops, and the goal is to find a set of train stations as small as possible such that every train visits at least one of the chosen stations. This problem can be modeled as a dominating set problem in a bipartite graph that has a vertex for each train and each station and an edge for each pair of a station and a train that stops at that station.[7]

A third example is in the academic field of numismatics. Ancient coins are made using two positive impressions of the design (the obverse and reverse). The charts numismatists produce to represent the production of coins are bipartite graphs.[8]

Suppose that two groups of people sign up for a dating service. After they've signed up, they are shown images of and given descriptions of the people in the other group. They are asked to select people that they would be happy to be matched with. All of the information is entered into a computer, and the computer organizes it in the form of a graph. The graph's vertices are the people, and there is an edge between them if they both said they would be happy to be matched with the other person. 


More abstract examples include the following:

    Every tree is bipartite.[4]
    Cycle graphs with an even number of vertices are bipartite
    
    
Bipartite graphs may be characterized in several different ways:

    A graph is bipartite if and only if it does not contain an odd cycle.[14]
    A graph is bipartite if and only if it is 2-colorable
        
    
'''