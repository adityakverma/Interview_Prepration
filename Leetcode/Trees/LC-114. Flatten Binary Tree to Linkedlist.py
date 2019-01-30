
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

#-------------------------------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Python Iterative O(n) time O(n) space solution
    # if a node has a left subtree, we will move it to the right , at the end, we will append the right tree!

    # Aditya: It simply flatten BST (InOrder wise) towards right side. Linked List word is misleading to me
    # This is purely a Tree question and has nothing to do with Linked List data structure.

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        stack = []

        while stack or root:
            if root.right:
                stack.append(root.right)

            if root.left:  # First flatten all left nodes 1,2,3,4, then add right nodes 5, 6 ( already saved on stacks) to flattened left
                root.right = root.left
                root.left = None
                root = root.right

            elif stack:
                root.right = stack.pop()
                root = root.right
            else:
                root = None

#############################################################

# This solution is adapted from this Java solution. You basically maintain a global variable
# prev which stores the last node that was flattened. First you flatten root.right, after which
# prev is root.right. Then you flatten root.left, which gets called recursively until you hit
# the 'end', at which point the flattened root.right is attached to the right of the 'end', and
# finally prev gets set to root.left. After the recursive calls, root.right get set to root.left,
# which already has the root.right attached to its end.

class Solution_(object):
    prev = None

    def flatten(self, root):
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


