
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
#
# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
#
# Example 1:
#
# Input:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

# =============================================================================
# See Image at : https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/160651/Python-DFS(node)-tm

class Solution(object):

    # Inspired by : https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/160651/Python-DFS(node)-tm

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1

        def dfs(root, level, index, start):
            if not root: return

            if len(start) == level:
                start.append(index)
                # print start
            else:
                self.res = max(self.res, index - start[level] + 1)

            print root.val, index, start, level, start[level]

            dfs(root.left, level + 1, index * 2, start)
            dfs(root.right, level + 1, index * 2 + 1, start)

        dfs(root, 0, 1, [])
        return self.res



'''
Your input

[1,3,2,5,3,null,9]

Your stdout

1 1 [1] 0 1
3 2 [1, 2] 1 2
5 4 [1, 2, 4] 2 4
3 5 [1, 2, 4] 2 4
2 3 [1, 2, 4] 1 2
9 7 [1, 2, 4] 2 4

Your answer

4

Expected answer

4
'''
