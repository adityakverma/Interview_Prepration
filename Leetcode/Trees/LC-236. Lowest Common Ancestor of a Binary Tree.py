
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: The lowest common ancestor is defined
# between two nodes p and q as the lowest node in T that has both p and q as descendants (
# where we allow a node to be a descendant of itself).
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
#              according to the LCA definition.

class Solution:             # Accepted
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):

        # escape condition
        if (not root) or (root == p) or (root == q):
            return root

        # search left and right subtree. Looks like Post Order.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # both found, root is the LCA
            return root
        return left or right

