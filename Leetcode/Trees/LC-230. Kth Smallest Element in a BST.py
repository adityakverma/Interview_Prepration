
# Given a binary search tree, write a function kthSmallest to find the
# kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# [Aditya]: Finding the kth smallest in a sorted array is easy, which is just nums[k-1].
# If we do a inorder traversal of the BST, the result will be the nodes in ascending order,
# then all we need is return inorder[k-1].
#
# Of course we are smarter than that. We do not need an array to store all the values
# during the traversal and we do not need to traversal the whole tree. Keeping a count of how
# many nodes have been traversaled allow us to return the node's value when count reaches k.

class Solution():

    def kthSmallest_recursive(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)

    # -----------------------------------

    def kthSmallest_iterative(self,root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


    def kthSmallest_iterative2(self, root, k):
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if not k:
                    break
                node = node.right
        return node.val


# averaged time: O(lg(n)+k)   ??







