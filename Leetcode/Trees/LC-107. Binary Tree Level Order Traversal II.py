
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# =============================================================================


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: # Else this fails one test case where input is []
            return []

        res, queue = [], [(root, 0)]
        while queue:
            node, level = queue.pop(0)

            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))    # Starts with left side first
            if node.right is not None:
                queue.append((node.right, level + 1))   # then right side

        return res[::-1] # Same as regular level order - just reverse the results.




