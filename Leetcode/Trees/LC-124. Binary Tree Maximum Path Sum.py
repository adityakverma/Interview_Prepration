
# 124. Binary Tree Maximum Path Sum
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from
# some starting node to any node in the tree along the parent-child
# connections. The path must contain at least one node and does not
# need to go through the root.

# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.current_max = float('-inf')

        def maxPathSumHelper(root):

            if not root:
                return 0

            left = maxPathSumHelper(root.left)
            right = maxPathSumHelper(root.right)

            left  = max(left, 0)
            right = max(right, 0)

            self.current_max = max(left + right + root.val, self.current_max)
            return max(left, right) + root.val

        maxPathSumHelper(root)
        return self.current_max



# class Solution(object):
# def init(self):
# self.globalmax = float("-inf")
#
#     def maxPathSum(self, root):
#         self.findmax(root)
#         return self.globalmax
#
#     def findmax(self, node):
#         if not node:
#             return 0
#         left = self.findmax(node.left)
#         right = self.findmax(node.right)
#         if left < 0: left = 0
#         if right < 0: right = 0
#         self.globalmax = max(left + right + node.val, self.globalmax)
#         return max(left, right) + node.val







