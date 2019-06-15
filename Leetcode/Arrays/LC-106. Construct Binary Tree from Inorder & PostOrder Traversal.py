
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34856/Discussion-on-Python-Solution

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # 12:00
    def buildTree(self, inorder_arr, postorder_arr):

        if not inorder_arr or not postorder_arr:
            return None

        root = TreeNode(postorder_arr.pop())    # We are making root using postorder array because in postorder root is travered last, so pop will give root node
        inorderIndex = inorder_arr.index(root.val) # Then we're figuring out the index of that root in inorder array and construct the tree.

        root.right = self.buildTree(inorder_arr[inorderIndex +1:], postorder_arr)
        root.left = self.buildTree(inorder_arr[:inorderIndex], postorder_arr)

        return root


if __name__ == '__main__':
    pass


