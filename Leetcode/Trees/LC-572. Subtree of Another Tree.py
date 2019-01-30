
# Tree , FB, EBAY
# This question is same as 100,101 ..

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# First, travel down the bigger tree via standard dfs, if we find node equal to the
# value of root of the smaller tree, compare the subtrees.
# We travel down both subtrees at the same time and if and only if every node is
# the same then we know we have found the right subtree.

class Solution(object):

    def isSubtree(self, t1, t2):

        if not t1:
            return False

        if t1.val == t2.val and self.checkTree(t1, t2):
            return True

        return self.isSubtree(t1.left, t2) or self.isSubtree(t1.right, t2)

    def checkTree(self, root1, root2):

        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False
        if root1.val != root2.val:
            return False

        return self.checkTree(root1.left, root2.left) and self.checkTree(root1.right, root2.right)

    # =============================================================================

    # Basically we convert our tree into string representation, then just check whether
    # substring exists in target string.

    def isSubtree_(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"

        return convert(t) in convert(s)

    # =============================================================================




# class Solution(object):
#     def isSubtree(self, s, t):
#         """
#         :type s: TreeNode
#         :type t: TreeNode
#         :rtype: bool
#         """
#         stack = [s]
#         while stack:
#             node = stack.pop()
#             if node.val == t.val and self.check(node, t):
#                 return True
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#
#         return False
#
#
#     def check(self, s1, t1):
#         # check the tree is the same or not
#         if s1 and t1 and s1.val == t1.val:
#             if self.check(s1.left, t1.left) and self.check(s1.right, t1.right):
#                 return True
#
#         if s1 is None and t1 is None:
#             return True

# -----------------------------------------------------------------------------

# The question is exactly similar to the Leetcode 100 Same Tree
# Solution for Leetcode 100: https://leetcode.com/problems/same-tree/discuss/148340/CPP-Easy-to-Understand
#
# Also Check Leetcode 101 [Symmetric Tree]https://leetcode.com/problems/symmetric-tree/description/)
# Leetcode 101 eh? :P
#
# Okay so now you will be absolutely comfortable with this question. It just requires you to
#
#     Start with a node of tree s (lets call this s-node)
#     Compare the trees forming with root s-node and root t
#     If the trees match(leetcode 100 logic) then return true
#     Else go to step one and check for s->left || s->right


