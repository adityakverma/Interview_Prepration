
# Given a binary tree rooted at root, the depth of each node is the shortest
# distance to the root.
#
# A node is deepest if it has the largest depth possible among any node in the
# entire tree.
# The subtree of a node is that node, plus the set of all descendants of that node.
#
# Return the node with the largest depth such that it contains all the deepest
# nodes in its subtree.

# Example 1:
#
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# ===============================================================================

class Solution(object):

    def countDepth(self, root):
        if root == None:
            return [0, None]

        ld, ln = self.countDepth(root.left)  # leftDepth, leftNode
        rd, rn = self.countDepth(root.right)  # rightDepth, rightNode

        if ld == rd:
            return [ld + 1, root]

        if ld < rd:
            return [rd + 1, rn]

        return [ld + 1, ln]

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.countDepth(root)[1]  # Note we are returning root of that subtree - self.countDepth(root)[1]



# Very good example to understand recursion - relate it with finding depth question.
# Once you reach depth of max and start returning recursively, then return depth and
# node value for each node. also compare left and right values and choose whose depth
# is greater.
