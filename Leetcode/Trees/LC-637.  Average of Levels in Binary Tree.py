
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
#
# Example 1:
#
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # Recursive method
    def averageOfLevels_Recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []

        def run(root, level):
            if root:
                if (len(res) <= level):
                    res.append([])
                res[level].append(root.val)

                run(root.left, level + 1)
                run(root.right, level + 1)
            return res

        temp = run(root, 0)
        # for i in temp:
        #    print i, sum(i), float ((sum(i)*1.0)/len(i))
        return [float((sum(i) * 1.0) / len(i)) for i in temp]

    # =================================================
    # Iterative method
    def averageOfLevels_Iterative(self, root):

        res = []
        if not root:
            return res
        q = [root]

        while q:
            total, cnt = 0, len(q)

            for _ in xrange(cnt):
                node = q.pop(0)
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(total * 1.0 / cnt)

        return res

    # ===============================================







