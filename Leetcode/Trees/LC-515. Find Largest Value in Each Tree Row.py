
# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]
# ======================================================================

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []

        def bfs(root):

            if root is None:
                return []

            queue = [(root, 0)]
            result = []

            while queue:
                node, level = queue.pop(0)

                if len(result) == level:
                    result.append([])
                result[level].append(node.val)

                if node.left is not None:
                    queue.append((node.left, level + 1))
                if node.right is not None:
                    queue.append((node.right, level + 1))

            return result

        s = bfs(root)
        for i in range(len(s)):
            self.ans.append(max(s[i]))

        return self.ans

