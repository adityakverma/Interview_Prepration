
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0,1] is the same as [1,0] and thus will not appear together in edges.
# -------------------------------------------------------------------------------------

# Basically this also reminds me of connected component - where we check DFS starting for every vertex,
# which will avoid checking if its one Tree/Graph or group of many.

import collections

class Graph():

    # Simple BFS: Trick: Using the equivalent definition of tree (a connected graph with n-1 edges),
    # we only need to check whether both the two conditions are satisfied. First construct
    # the graph, and then BFS from node 0 to see if all nodes can be visited (thus connected).
    # Finally check if there are exactly n-1 edges.

    # BFS with Queue
    def validTree_BFS_Queue(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)  # Basically this is Graph

        for i, j in edges:
            graph[i].add(j) # Notice how we build an undirected graph: include both edges.
            graph[j].add(i)

        queue = [0]
        visited = [0] * len(graph)

        while queue:
            cur = queue.pop(0)
            for neighbour in graph[cur]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return len(visited)==n and len(edges)==n-1

    # DFS with Stack
    def validTree_DFS_Stack(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)  # Basically this is Graph

        for i, j in edges:
            graph[i].add(j) # Notice how we build an undirected graph: include both edges.
            graph[j].add(i)

        stack = [0]
        visited = [0] * len(graph)

        while stack:
            cur = stack.pop()
            for neighbour in graph[cur]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

        return len(visited)==n and len(edges)==n-1



    # DFS with Stack - Different though process
    def validTree_DFS(self, n, edges):

        dic = {i: set() for i in xrange(n)} # Basically this is Graph

        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)  #  Since Undirected Graph

        stack = [dic.keys()[0]]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbour in dic[node]:
                stack.append(neighbour)
                dic[neighbour].remove(node)
            dic.pop(node)
        return not dic


if __name__ == '__main__':

    g = Graph()
    n =5
    #edges = [[0,1], [0,2], [0,3], [1,4]]
    edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    print "\nIs Graph Valid Tree ? ", g.validTree_BFS_Queue(n, edges)
    print "\nIs Graph Valid Tree ? ", g.validTree_DFS_Stack(n, edges)

    print "\nIs Graph Valid Tree ? ", g.validTree_DFS(n, edges)

######################

'''
Simple BFS:

# Trick: Using the equivalent definition of tree (a connected graph with n-1 edges), 
# we only need to check whether both the two conditions are satisfied. First construct 
# the graph, and then BFS from node 0 to see if all nodes can be visited (thus connected). 
# Finally check if there are exactly n-1 edges.

class Solution(object):

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        queue = [0]
        visited = set([0])
        while queue:
            cur = queue.pop(0)
            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return len(visited)==n and len(edges)==n-1


# Method 2:

    def validTree_BFS(self, n, edges):

        dic = {i: set() for i in xrange(n)} # Graph

        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)

        visited = set()
        queue = collections.defaultdict(set) #collections.deque([dic.keys()[0]])

        while queue:
            node = queue.pop(0) # popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbour in dic[node]:
                queue.append(neighbour)
                dic[neighbour].remove(node)
            dic.pop(node)

        return not dic # Meaning at the end of BFS. Nothing should be left in dic if BFS traversal is completed.
        
        
'''