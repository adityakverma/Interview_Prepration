
# You need to construct a string consists of parenthesis and integers from a binary tree with the
# preorder traversing way.
#
# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all
# the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the
# string and the original binary tree.
#
# Example 1:
#
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"
#
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".
#
# Example 2:
#
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# Output: "1(2()(4))(3)"
#
# Explanation: Almost the same as the first example,
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the
# input and the output

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    result = " "
    def tree2str(self, t):

        if t is None:
            return

        self.result += str(t.val)

        self.result += "("
        self.tree2str(t.left)
        self.result += ")"

        self.result += "("
        self.tree2str(t.right)
        self.result += ")"

        self.result = self.result.replace('()()', '')
        self.result = self.result.replace('())', ')')
        self.result = self.result.replace(')()',')')

        return self.result


if __name__ == '__main__':

    s = Solution()
if __name__ == '__main__':

    s = Solution()
    # Driver code
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print s.tree2str(root)



'''

# My previous solution.

class Solution(object):
    def tree2str(self, node):
        """
        :type t: TreeNode
        :rtype: str
        """

        if not node:
            return ""
        else:
            result =  str(node.val)+"("+self.tree2str(node.left)+")"+"("+self.tree2str(node.right)+")" 
            
        result = result.replace('()()', '')
        result = result.replace('())', ')')
        result = result.replace(')()',')')
        return result 
        
'''