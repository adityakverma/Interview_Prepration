
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
# -----------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTarget(self, root, k):

        self.d = set()

        def dfs(root, k):
            if root is None:
                return False

            if root.val in self.d:
                return True
            else:
                self.d.add(k - root.val)

            return dfs(root.left, k) or dfs(root.right, k)

        return dfs(root, k)

    # ---------------------------------------------------------------

    def findTarget_(self, root, k):
        a = set()
        self.f = False

        def dfs(root, k):
            if not root:
                return

            if root.val in a:
                self.f = True
            else:
                a.add(k - root.val)

            dfs(root.left, k)
            dfs(root.right, k)

        dfs(root, k)
        return self.f


# Since it's a BST, a better solution would take advantage of it by using two pointers pointing at the smallest and the largest.

