
#  Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.

# Same as LC-687
class Solution(object):

    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter

# -------------------------------------------------------------

# Let's calculate the depth of a node in the usual way:
# max(depth of node.left, depth of node.right) + 1. While we do, a path "through" this node
# uses 1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node and remember
# the highest number of nodes used in some path.

# class Solution(object):
#
#     def diameterOfBinaryTree(self, root):
#
#         self.ans = 1   # Global variable
#         def depth(node):
#             if not node: return 0
#             L = depth(node.left)
#             R = depth(node.right)
#             self.ans = max(self.ans, L+R)
#             return max(L, R) + 1
#
#         depth(root)
#         return self.ans

# --------------------------------------------------------------

#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         class maxLen:
#             def __init__(self):
#                 self.max_len = 0
#
#         def treeHeightHelper(root, res):
#             if not root:
#                 return 0
#             lheight = treeHeightHelper(root.left, res)
#             rheight = treeHeightHelper(root.right, res)
#             res.max_len = max(res.max_len, lheight+rheight)
#             return 1 + max(lheight, rheight)
#
#         res = maxLen()
#         treeHeightHelper(root, res)
#         return res.max_len

# --------------------------------------------------------------

# The inner function is required in your solution to keep track of the global "self.ans" (the diameter).
# An alternative to an inner function solution can be passing the diameter parameter along with each
# recursive call and updating it when needed. This diameter parameter needs to be passed-by-reference,
# so you wrap in in an list.

# class Solution(object):
#
#     def diameterOfBinaryTree(self, root):
#         diameter = [0]
#         self.depth(root, diameter)
#         return diameter[0]
#
#     def depth(self, root, diameter):
#         if not root:
#             return 0
#         left_height = self.depth(root.left, diameter)
#         right_height = self.depth(root.right, diameter)
#         diameter[0] = max(diameter[0], left_height + right_height)
#         return 1 + max(left_height, right_height)

# --------------------------------------------------------------

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/133736/iterative-and-recursive-python-solutions


