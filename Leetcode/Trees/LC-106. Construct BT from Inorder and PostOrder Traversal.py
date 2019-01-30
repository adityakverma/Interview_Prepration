
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#

# postorder = [9,15,7,20,3] # Do postorder.pop() to get root of tree -  becasue last element will be root of tree since its POSTorder
# inorder = [9,3,15,20,7]   # Left of root will left subtree and right of root will be Right subtree since its Inorder

# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# --------------------------------- My Solution ACCEPTED ----------------------------------------

class TreeNode:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):

        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())  # postorder.pop() because lasr element will be root of tree since its POSTorder. For PreOrder, we do postorder.pop(0)
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder) # Reason we have right first - need to build the tree from right to left, because we are popping from the last element from the postorder array.
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

# ----------------------------------------------------------------------------------------------------


# Construct Binary Tree from Preorder and Inorder Traversal, Solution

# http://fisherlei.blogspot.com/2013/01/leetcode-construct-binary-tree-from.html

#  There is an example.
#
#         _______7______
#        /              \
#     __10__          ___2
#    /      \        /
#    4       3      _8
#             \    /
#              1  11
#
# The preorder and inorder traversals for the binary tree above is:
#
# preorder = {7,10,4,3,1,2,8,11}
# inorder = {4,10,3,1,7,11,8,2}
#
#
# The first node in preorder alwasy the root of the tree. We can break the tree like:
# 1st round:
# preorder:  {7}, {10,4,3,1}, {2,8,11}
# inorder:     {4,10,3,1}, {7}, {11, 8,2}
#
#         _______7______
#        /              \
#     {4,10,3,1}       {11,8,2}
#
# Since we alreay find that {7} will be the root, and in "inorder" set, all the data in the left of {7} will construct the left sub-tree. And the right part will construct a right sub-tree. We can the left and right part agin based on the preorder.
# 2nd round

#               left part                                                 right part
# preorder: {10}, {4}, {3,1}                                              {2}, {8,11}
# inorder:  {4}, {10}, {3,1}                                               {11,8}, {2}
#
#
#         _______7______
#        /              \
#     __10__          ___2
#    /      \        /
#    4      {3,1}   {11,8}
#
# see that, {10} will be the root of left-sub-tree and {2} will be the root of right-sub-tree.
#
# Same way to split {3,1} and {11,8}, yo will get the complete tree now.
#
#         _______7______
#        /              \
#     __10__          ___2
#    /      \        /
#    4       3      _8
#             \    /
#              1  11
#
# So, simulate this process from bottom to top with recursion as following code.

# --------------------------------------------------------------------------------------------

# def buildTree(self, inorder, postorder):
#     if inorder:
#         ind = inorder.index(postorder.pop())
#         root = TreeNode(inorder[ind])
#         root.right = self.buildTree(inorder[ind+1:], postorder)
#         root.left = self.buildTree(inorder[:ind], postorder)
#         return root

# ------------------------------------------------------------------------------

# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         """
#         :type inorder: List[int]
#         :type postorder: List[int]
#         :rtype: TreeNode
#         """
#         if inorder:
#             ind = inorder.index(postorder.pop())
#             root = TreeNode(inorder[ind])
#             root.left = self.buildTree(inorder[:ind],postorder)
#             root.right = self.buildTree(inorder[ind+1:],postorder)
#             return root
#
# Could you help me understand why this is throwing an error ? Thank you for your help in advance.
# I guess its because in postorder we have
# left,right,middle elements so we have to first construct middle node, then right node and then left node. very concise code for both 106. Construct Binary Tree from Inorder and Postorder Traversal and 105 Construct Binary Tree from Preorder and Inorder Traversal problems

# need to build the tree from right to left, because we are popping from the last element from the postorder array.
# ------------------------------------------------------------------------------



