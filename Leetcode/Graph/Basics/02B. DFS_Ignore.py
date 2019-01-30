# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

# Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of
# a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may
# come to the same node again. To avoid processing a node more than once, we use a
# boolean visited array.

# Python program to print DFS traversal from a given given graph

#  [ADITYA] : THIS IS DFS USING RECURSION.
#  ALTERNATIVELY WE CAN ALSO DO 'DFS' BY ITERATIVE METHOD USING STACK

############################  IMPORTANT ##########################################

# [ADITYA]: ITERATIVE METHOD FOR BFS AND DFS ARE EXACTLY SAME IN GRAPH- EXCEPT USE
# OF STACK IN DFS (and stack.pop()) AND USE OF QUEUE IN BFS ALGO ( AND queue.pop(0)
# OR queue.popleft() IF WE USED collections.deque

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

    def DFS_aditya(self, source):

        stack = []
        stack.append(source) # We append first so looks like PreOrder DFS - similar to tree.

        dist = defaultdict(list)
        dist[source] = 0

        while stack:
            node = stack.pop()
            print node, # OR result.append(node)

            for neighbour in self.graph[node]:
                if neighbour not in dist:
                    dist[neighbour] = dist[node] +1
                    stack.append(neighbour)

        print "\nDistance map is ",(dist.items()) # Additional Info


    '''
    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print v,

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited) # We are going into depth to next level by this recursive call.
    
    
    # The function to do DFS traversal. It uses recursive DFSUtil()
    # This is from Geekforgeek which doesn't work if new vertex is added (1,4)
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        #print (len(self.graph))

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)
    '''
    # -------------------------------------------------------------
    '''
    def DFS_Iterative(self, src):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        stack= []
        stack.append(src) # We append first so looke like PreOrder DFS - similar to tree.

        visited[src] = True

        while stack:
            node = stack.pop()
            print node, # OR result.append(node)

            for neighbour in self.graph[node]:
                if visited[neighbour] == False:
                    stack.append(neighbour)
                    visited[neighbour] = True '''

    # -------------------------------------------------------------

                    

    '''
    #######################################################################################

    # DFS iteratively # [Aditya] : This is exactly same as Graph BFS using queue - Only 
    # difference is here we use STACK and do stack.pop(). Check BFS Iterative  using queue 
    
    def cloneGraph2(self, node):
        if not node:
            return
            
        nodeCopy = UndirectedGraphNode(node.label)  # Extra : Creating node copy for clone graph
        dic = {node: nodeCopy}                      # Extra : Creating map for clone graph
        stack = [node]
        
        while stack:
            node = stack.pop()          # Seems like PreOrder Traversal where we pop root first.
            for neighbor in node.neighbors:
                if neighbor not in dic:
                
                    neighborCopy = UndirectedGraphNode(neighbor.label)  # Extra : Creating neighbour copy for clone graph
                    dic[neighbor] = neighborCopy                        # Extra : Filling up for clone
                    dic[node].neighbors.append(neighborCopy)            # Extra : Appending neighbour of clone
                    
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    #######################################################################################

    # DFS recursively # [Aditya]: This is same as Above Recursive DFS
    
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
            
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

    ####################################################################################### '''


# Driver code create a graph given in the above diagram
if __name__ == '__main__':

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(1, 4)

    print "\nFollowing is DFS from (starting from vertex 2): "
    # print "\n\nDFS Recursive:",
    #g.DFS(2)
    #
    # print "\nDFS Iterative:",
    # g.DFS_Iterative(2)

    print "\nDFS Aditya   :",  # Only This gives correct answer when we add extra node (1,4). Doing via geekforgeek gives error.
    g.DFS_aditya(2)

























##############################################################

'''
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
    def DFSUtil(self, node, dist):
        print node,
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[node]:
            if neighbour not in dist.keys():
                dist[neighbour] = dist[node] + 1  # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
                self.DFSUtil(neighbour, dist)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self ,source):
        dist = defaultdict(list) # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
        dist[source]=0           # <=== Extra compared to Geekforgeek since we're trying to maintain distance map
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(source, dist)

        print "\nDistance map",\
        dist.items()


################### Driver code ##############################
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "\nFollowing is DFS from (starting from vertex 2): ",
g.DFS(2)

'''