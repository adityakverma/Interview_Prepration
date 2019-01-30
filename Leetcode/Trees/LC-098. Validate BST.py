
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
# Input:
#     2
#    / \
#   1   3
# Output: true
#
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# [Aditya]: My idea: Given a tree, do its inorder traversal. If its in ascending order
# then its a BST, else not.

########################################################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isValidBST(self, root):
        self.last = -float('inf')
        self.flag = True

        self.inorder(root)
        return self.flag

    def inorder(self, root):

        if not root:
            return

        self.inorder(root.left)

        if self.last >= root.val:
            self.flag = False
        self.last = root.val

        self.inorder(root.right)

###################################################################

# Alternate way : same concept:
'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

'''

################## Iterative using Stack #################################

#
# class Solution(object):
#     def isValidBST(self, root):

#         if not root:return True

#         stack=[]
#         res=[]
#         while root or stack:
#             if root:
#                 stack.append(root)
#                 root=root.left
#             else:
#                 root=stack.pop()
#                 res.append(root.val)
#                 root=root.right

#         if res==sorted(res) and len(res)==len(set(res)):
#             return True
#         else:return False
#

#################################################################################












'''
# Sorted Array to Balanced BST :
# Concept is Find mid value. left of index.A[mid] will form left subtree and right of index.A[mid] will be right subtree.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, A):
        if len(A) == 0:
            return None
        mid = len(A) / 2
        root = TreeNode(A[mid])

        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root

'''
