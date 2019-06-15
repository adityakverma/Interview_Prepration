
# You need to construct a string consists of parenthesis and integers from a binary tree
# with the pre-order traversing way.
# The null node needs to be represented by empty parenthesis pair "()". And you need to
# omit all the empty parenthesis pairs that don't affect the one-to-one mapping
# relationship between the string and the original binary tree.
#
# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"

# Explanation: Originally it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, node):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not node:
            return ""
        else:
            result = str(node.val) + "(" + self.tree2str(node.left) + ")" + "(" + self.tree2str(node.right) + ")"

        result = result.replace('()()', '')
        result = result.replace('())', ')')
        result = result.replace(')()', ')')
        return result

if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)

    s = Solution()
    print "\nString is:",s.tree2str(root)

# Complexity Analysis
#     Time complexity : O(n). The preorder traversal is done over the n nodes of the given Binary Tree.
#     Space complexity : O(n). The depth of the recursion tree can go upto n in case of a skewed tree.
#
# ------------------------------------------------------------------------------------------------------



# FYI:

    # def tree2str(self, t):  # This also WORKS !
    #     """
    #     :type t: TreeNode
    #     :rtype: str
    #     """
    #     if not t:
    #         return ""
    #     s = str(t.val)
    #
    #     if not t.left and t.right:
    #         s += "()(" + self.tree2str(t.right) + ")"
    #     else:
    #         if t.left:
    #             s += "(" + self.tree2str(t.left) + ")"
    #         if t.right:
    #             s += "(" + self.tree2str(t.right) + ")"
    #     return s


# Next challenges: LC-536: Construct Binary Tree from String


