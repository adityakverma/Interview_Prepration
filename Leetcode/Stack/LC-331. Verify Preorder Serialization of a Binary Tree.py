
# One way to serialize a binary tree is to use pre-order traversal. When we encounter a
# non-null node, we record the node's value. If it is a null node, we record using a
# sentinel value such as #.
#
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
#
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
# where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct preorder traversal
# serialization of a binary tree. Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a character '#'
# representing null pointer.
#
# You may assume that the input format is always valid, for example it could never contain two
# consecutive commas such as "1,,3".
# ==========================================================================================

# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78560/Simple-Python-solution-using-stack.-With-Explanation.

# By replacing the top with hash you are shrinking tree's child to
# null because you already process the child and all it's children.

# In very easy way I would say imagine popping from the stack as folding of
# the tree. The basic intuition was to collapse the entire tree into the root node.

#  we convert a node with two children null nodes into a null node. We continue
# doing this, either iteratively or recursively, until we are left with just a null node.

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        top = -1
        preorder = preorder.split(',')

        for s in preorder:
            stack.append(s)
            top += 1

            while(self.endsWithTwoHashes(stack,top)):
                h = stack.pop()
                top -= 1
                h = stack.pop()
                top -= 1

                if top < 0:
                    return False

                h = stack.pop()
                stack.append('#')

        if len(stack) == 1:
            if stack[0] == '#':
                return True
        return False

    def endsWithTwoHashes(self,stack,top):
        if top<1:
            return False
        if stack[top]=='#' and stack[top-1]=='#':
            return True
        return False
