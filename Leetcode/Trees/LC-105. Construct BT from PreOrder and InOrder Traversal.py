

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# ------------------------------- My Solution - ACCEPTED ---------------------

class TreeNode:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None

class Solution(object):

    def buildTree(self, preorder, inorder):

        if not inorder or not preorder:
            return None

        root = TreeNode(preorder.pop(0))  # preorder.pop(0) because first element will be root of tree
        inorderIndex = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:inorderIndex])  # Reason we have left first - need to build the tree from left to right, because we are popping from the first element from the preorder array.
        root.right = self.buildTree(preorder, inorder[inorderIndex + 1:])

        return root

# ------------------------------------------------------------------------------

# Leetcode Solution: Almost same - but they used deque to get popleft, instead of my way using pop(0)
'''
     
from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder, inorder):
            if not inorder:
                return None
            
            # pick up the first element as a root
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = inorder.index(root_val)

            # recursion 
            root.left= helper(preorder, inorder[:index])
            root.right = helper(preorder, inorder[index + 1:])
            return root
        
        return helper(deque(preorder), inorder)
        
'''
        
# Complexity analysis
# -------------------
#    Time complexity : the popleft operation is cheap O(1), but searching in the inorder list
#    and the construction of inorder lists for the left and right subtrees take O(N), where N
#    is a number of nodes in the tree. Therefore the time complexity is O(N)\mathcal{O}(N)O(N).

#    Space complexity : O(N), since we store the entire tree.
        
