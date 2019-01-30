
# Given a non-empty special binary tree consisting of nodes with the non-negative
# value, where each node in this tree has exactly two or zero sub-node. If the
# node has two sub-nodes, then this node's value is the smaller value among its
# two sub-nodes.
#
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
#
# Input:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
# # ==========================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import heapq

        min_heap = []
        k = 2
        output = -1  # Required for code to get ACCEPTED.

        def preorder(node):

            if node is None:
                return

            if (not min_heap or node.val > abs(min_heap[0])):
                heapq.heappush(min_heap, node.val)

            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)

        preorder(root)

        if len(min_heap) >= k:
            while k:
                output = heapq.heappop(min_heap)
                k -= 1

        return output

