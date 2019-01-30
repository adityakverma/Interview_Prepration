
# Return any binary tree that matches the given preOrder and postOrder
# traversals.
# Values in the traversals pre and post are distinct positive integers.

# Example 1:
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]

# =====================================================================

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# The first value of 'pre' and last value of 'post' is 'root'. Find the second value of
# 'pre' in 'post' as it is the left child of 'root'. From here, we divide pre and post
# into left branch and right branch.

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        if not pre: return

        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]

        # print "pre[1:]", pre
        # print "post[:-1]", post

        if not pre: return root

        i = post.index(pre[0])
        # print "i..",i

        # print "Left",pre[:i+1], post[:i+1]
        # print "Right",pre[i+1:], post[i+1:]

        root.left = self.constructFromPrePost(pre[:i + 1], post[:i + 1])
        root.right = self.constructFromPrePost(pre[i + 1:], post[i + 1:])

        return root