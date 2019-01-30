
#  Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
# Example 2:
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7

# ============================================================

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def bfs(root, level):
            if root:
                if (len(res) <= level):
                    res.append([])
                res[level].append(root.val)

                bfs(root.left, level + 1)
                bfs(root.right, level + 1)
            return res

        temp = bfs(root, 0)
        #print temp, temp[-1][0]
        return temp[-1][0]





