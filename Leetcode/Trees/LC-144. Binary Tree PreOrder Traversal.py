
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Base Case
        if root is None:
            return []

        result = []
        stack = []
        stack.append(root) # We append because we want root first in preOrder

        while(stack):

            node = stack.pop()
            result.append(node.val)

            # Push right and left children of the popped node to stack
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result
