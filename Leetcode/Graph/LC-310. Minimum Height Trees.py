
# For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Example 1 :
#
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
#
# Output: [1]
#
# Example 2 :
#
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
#
# Output: [3, 4]

# Note:
#
#  According to the definition of tree on Wikipedia: a tree is an undirected graph
#  in which any two vertices are connected by exactly one path. In other words, any
#  connected graph without simple cycles is a tree.

#  The height of a rooted tree is the number of edges on the longest downward path
#  between the root and a leaf.
# -----------------------------------------------------------------------------------

# [Aditya]: We can solve this problem by first thinking about 1-D solution, that is if a longest
# graph is given, then the node which will minimize the height will be mid node if total
# node count is odd or mid two node if total node count is even. This solution can be
# reached by following approach - Start two pointers from both end of the path and move
# one step each time, until pointers meet or one step away, at the end pointers will be
# at those nodes which will minimize the height because we have divided the nodes evenly
# so height will be minimum.
# Same approach can be applied to a general tree also. Start pointers from all leaf nodes
# and move one step inside each time, keep combining pointers which overlap while moving,
# at the end only one pointer will remain on some vertex or two pointers will remain at
# one distance away. Those node represent the root of the vertex which will minimize the
# height of the tree.
# So we can have only one root or at max two root for minimum height depending on tree
# structure as explained above. For implementation we will not use actual pointers instead
# we will follow BFS like approach, In starting all leaf node are pushed into the queue,
# then they are removed from tree, next new leaf node are pushed in queue, this procedure
# keeps on going until we have only 1 or 2 node in our tree, which represent the result.
# As we are accessing each node once, total time complexity of solution is O(n).

# https://leetcode.com/problems/minimum-height-trees/discuss/76075/Python-solution-with-detailed-explanation
# https://leetcode.com/problems/minimum-height-trees/discuss/130545/python:-min-ht-trees-by-trimming-leaves

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]

        graph = [set() for _ in xrange(n)]
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        # the intuition is that in a connected graph,
        # if you pick a node of degree 1 as the root
        # then the resulting tree has the max ht.
        # so trim the leaves until there are at most 2
        # and at least 1 node left.

        leaves = [i for i in xrange(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1: new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves





