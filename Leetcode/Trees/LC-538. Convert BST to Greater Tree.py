
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original
#  BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
###################################################################

# [Aditya]: Explanation: General idea is doing a reverse Inorder traversal, and adding
# to the sum as you go for the creation of the new tree.


# This question asks us to modify an asymptotically linear number of nodes in a given
# binary search tree, so a very efficient solution will visit each node once. The key
# to such a solution would be a way to visit nodes in descending order, keeping a sum
# of all values that we have already visited and adding that sum to the node's values
# as we traverse the tree. This method for tree traversal is known as a reverse in-order
# traversal, and allows us to guarantee visitation of each node in the desired order.
# The basic idea of such a traversal is that before visiting any node in the tree, we
# must first visit all nodes with greater value.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursion Solution :
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:

            self.convertBST(root.right)

            self.total += root.val
            root.val = self.total

            self.convertBST(root.left)

        return root

# -------------------------------------------------------
# Complexity Analysis
#
#     Time complexity : O(n)
#     A binary tree has no cycles by definition, so convertBST gets called on each node no
#     more than once. Other than the recursive calls, convertBST does a constant amount of
#     work, so a linear number of calls to convertBST will run in linear time.
#
#     Space complexity : O(n)
#     Using the prior assertion that convertBST is called a linear number of times, we can
#     also show that the entire algorithm has linear space complexity. Consider the worst
#     case, a tree with only right (or only left) subtrees. The call stack will grow until
#     the end of the longest path is reached, which in this case includes all nnn nodes.

###########################################################

# Iterative method using Stack:

class Solution1(object):
    def convertBST(self, root):
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root

# One way to describe the iterative stack method is in terms of the intuitive recursive solution.
#  First, we initialize an empty stack and set the current node to the root. Then, so long as
# there are unvisited nodes in the stack or node does not point to null, we push all of the nodes
# along the path to the rightmost leaf onto the stack. This is equivalent to always processing
# the right subtree first in the recursive solution, and is crucial for the guarantee of visiting
#  nodes in order of decreasing value. Next, we visit the node on the top of our stack, and
# consider its left subtree. This is just like visiting the current node before recursing on
# the left subtree in the recursive solution. Eventually, our stack is empty and node points
# to the left null child of the tree's minimum value node, so the loop terminates.

