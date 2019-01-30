
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Return 24.
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root): # Kind of PreOrder
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0

        def dfs(root):

            if not root:
                return 0

            if root.left and not root.left.left and not root.left.right:
                self.sum += root.left.val

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.sum



    # Idea is very simple. Just traverse the whole tree using stack. If the left child is leave, add it to the result.

    def sumOfLeftLeaves_Iterative(self, root):
        if not root: return 0

        s = [root]
        res = 0
        while s:
            tmp = s.pop()

            if tmp.left:
                s.append(tmp.left)

                if not tmp.left.left and not tmp.left.right:
                    res += tmp.left.val

            if tmp.right:
                s.append(tmp.right)

        return res
