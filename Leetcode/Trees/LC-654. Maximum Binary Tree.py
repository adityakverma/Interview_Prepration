
#  Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
#     The root is the maximum number in the array.
#     The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#     The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
#
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1

# This is also called a Cartesian Tree. One interesting property is that if we do an
# in-order traversal, we get the array back which we used to create it.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # Something like divide and conquer solution
    def constructMaximumBinaryTree(self, nums):

        if not nums:
            return None

        root = TreeNode(max(nums))
        idx = nums.index(max(nums))

        if len(nums[:idx]) > 0:
            root.left = self.constructMaximumBinaryTree(nums[:idx])

        if len(nums[idx + 1:]) > 0:
            root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return root


# Complexity Analysis
#     Time complexity : O(n^2). The function construct is called nnn times. At each level of the recursive tree, we traverse over all the nnn elements to find the maximum element. In the average case, there will be a log(n)log(n)log(n) levels leading to a complexity of O(nlog(n))O\big(nlog(n)\big)O(nlog(n)). In the worst case, the depth of the recursive tree can grow upto nnn, which happens in the case of a sorted numsnumsnums array, giving a complexity of O(n2)O(n^2)O(n2).
#     Space complexity : O(n). The size of the setsetset can grow upto nnn in the worst case. In the average case, the size will be log(n)log(n)log(n) for nnn elements in numsnumsnums, giving an average case complexity of O(log(n))O(log(n))O(log(n))

# More about Cartesian Tree -
# https://en.wikipedia.org/wiki/Cartesian_tree
# In computer science, a Cartesian tree is a binary tree derived from a sequence of
# numbers; it can be uniquely defined from the properties that it is heap-ordered
# and that a symmetric (in-order) traversal of the tree returns the original sequence.

# IMP: Cartesian trees may be used as part of an efficient data structure for range
# minimum queries, a range searching problem involving queries that ask for the minimum
# value in a contiguous subsequence of the original sequence.[2] In a Cartesian tree,
# this minimum value may be found at the lowest common ancestor of the leftmost and
# rightmost values in the subsequence. For instance, in the subsequence (12,10,20,15)
#  of the sequence shown in the first illustration, the minimum value of the subsequence
# (10) forms the lowest common ancestor of the leftmost and rightmost values (12 and 15).
#  Because lowest common ancestors may be found in constant time per query, using a data
# structure that takes linear space to store and that may be constructed in linear time,
# [3] the same bounds hold for the range minimization problem.


