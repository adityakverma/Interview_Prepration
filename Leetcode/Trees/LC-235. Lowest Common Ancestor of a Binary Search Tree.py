#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
#
# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
#              according to the LCA definition.

# [ADITYA]: To me this looks more like FIRST common ancestor than Lowest common ancestor.

class Solution():

    # Iterative method
    def lowestCommonAncestor_01(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

    # Uiing DFS ( Post Order)/ Recursion
    def lowestCommonAncestor_02(self, root, p, q):

        if not root or not p or not q:
            return None

        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor_01(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor_02(root.right, p, q)
        else:
            return root

# > Time Complexity O(h)
# > Space Complexity O(1)

