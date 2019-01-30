
# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# Bonus points if you could solve it both recursively and iteratively.
# Official Solution: https://leetcode.com/problems/symmetric-tree/solution/#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Recursive
    # TC: O(b) SC: O(log n)
    def isSymmetric(self, root):

        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)


    def isMirror(self, left, right):

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val != right.val:
            return False
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    # In this sub routine we can also say T1 and T2 for left and right substree instead of
    # left and right - Note this is similar to LC-100 Same Tree problem. Only minor difference
    # in the logic of same (Same) vs mirror (Symmetric)

    def isSymmetric_Iterative(self, root):

        if not root:
            return True

        queue = []
        queue.append((root.left, root.right))

        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False

            queue.append((l.left, r.right))
            queue.append((l.right, r.left))

        return True

#######################################################

# The essence of recursively is Stack, so we can use our own stack to rewrite it into iteratively:

class Solution2:

    def isSymmetric(self, root):
        if root is None:
          return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False

            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True