
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def mergeTree_Recursive(self, t1, t2):
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2

    # Note: Here in we are adding sums in tree T1 itself, so no need to make
    # new tree T3 like T3 = T2 + T1

    def mergeTree_Iterative(self, t1, t2):
        if t1 is None:
            return t2

        stack = []
        stack.append((t1, t2))

        while stack:
            t = stack.pop()  # Note: This gives t[0] which is t1 that was pushed; and t[1] that was t2 pushed on stack.
                             # Once value are pushed, we deal with stack values ( like pop etc) and do no consider original t1 and t2.
            if t[1] is None: # If t2's value is None then nothing to add. t1's value is final. Look for others on stack.
                continue

            t[0].val += t[1].val

            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))

            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1

    def mergeTrees(self, t1, t2):

        # return self.mergeTree_Recursive(t1, t2)
        return self.mergeTree_Iterative(t1, t2)

########################################################################################




class Solution1(object):  # Accepted

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        elif not t1 and t2:
            return t2
        elif t1 and not t2:
            return t1
        else:
            t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

