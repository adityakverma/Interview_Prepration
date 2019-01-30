

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left  # Keep pushing left elements till end
            else:
                root = stack.pop()  # Else pop root and then check right elements.
                res.append(root.val)
                root = root.right

        return res

