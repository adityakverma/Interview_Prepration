
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than or equal to the node's key.
#     The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
#     Both the left and right subtrees must also be binary search trees.
#
#
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
#
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
# ================================================================================

# O(N) time & O(N) Space
#
#     Use a dictionary to store the frequency of each interger. Then simply find the largest frequency and return all the associated keys.
#     Note we do not use the property of BST in this solution.

import collections


class Solution(object):

    def findMode(self, root):  # USING COUNTER
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = collections.Counter()

        if root is None:
            return []

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_ct]

    # -----------------------------------------------------------------

    def findMode_(self, root):  # USING DICT
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}

        def DFS(node):
            if node:
                count[node.val] = count.get(node.val, 0) + 1
                DFS(node.left)
                DFS(node.right)

        if not root:
            return []

        DFS(root)
        most_frequent = max(count.values())

        res = [n for n, f in count.items() if f == most_frequent]

        return res

# --------------------------------------------------------------------
# O(N) time and O(1) Space
#
#     Write BST Iterator class which gives the next element in_order. Now the problem reduces to finding mode in a sorted array.
#     Instead of a BST iterator, we can use a recursive inorder traversal and store a class variable pre to indicate the previous integer.
#     https://discuss.leetcode.com/topic/77308/4ms-java-solution-beats-100-o-1-space-recursion-stack-space-doesn-t-count
#
# Divide and Conquer
#
#     Mode lies entirely in left subtree, or in right subtree or the middle element is the mode.
#     Time would be NlogN at best and space O(1)

#---------------------------------------------------------------------------



# from collections import defaultdict
# class Solution(object):
#     def helper(self, root, cache):
#         if root == None:
#             return
#         cache[root.val] += 1
#         self.helper(root.left, cache)
#         self.helper(root.right, cache)
#         return
#
#     def findMode(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return []
#         cache = defaultdict(int)
#         self.helper(root, cache)
#         max_freq = max(cache.values())
#         result = [k for k,v in cache.items() if v == max_freq]
#         return result

