
# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
#
# Example:
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

# [Aditya]: Algo - Keep appending path till we reach leaf node [if not root.left and not root.right ].
# Once it reaches leaf node - Append whole path to result.

class Solution(object):

    # ----------------------------------- Recursion [ACCEPTED] ----------------------------------------------

    def binaryTreePaths_(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, path, res):

        if not root.left and not root.right: # We only append when it reached leaf. Before that we keep appending to path.
            res.append(path + str(root.val))

        if root.left:
            self.dfs(root.left, path + str(root.val) + "->", res)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", res)

    # --------------------------- Iterative = DFS + Stack [ACCEPTED] -------------------------------------

    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")] # This is like calling dfs function in above

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right: # We only append when it reached leaf. Before that we keep appending to path.
                res.append(path + str(node.val))

            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))

        return res

    # -------------------------------------------------------------------------------------------
    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res

    # -------------------------------------------------------------------------------------------




###################################################################################

# Another variation:
# Given a binary tree and a sum, find all root-to-leaf paths where each paths sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

'''
# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

######################## Aditya's Solution ##################################

check = 7
s = []
# @param A : root node of tree
# @param B : integer
# @return an integer
def Aditya_return_Allpaths(A, check ,val):
    if A == None:
        return False

    s.append(A.val)
    val += A.val
    if A.left == None and A.right == None and val == check:
        return s

    return Aditya_return_Allpaths(A.left, check, val) or Aditya_return_Allpaths(A.right, check, val)

######################## Interview-Bits Solution ################################

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        res = []

        def helper(A, sums, arr):
            if not A:
                return
            if not A.left and not A.right:
                if sums == A.val:
                    res.append(arr + [A.val])
                return
            helper(A.left, sums - A.val, arr + [A.val])
            helper(A.right, sums - A.val, arr + [A.val])

        helper(root, sum1, [])
        return res
#################################################

# Driver program to test above functions
root = Node(1)

root.left  = Node(2)
root.left.left  = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.left = Node(3)
root.right.right = Node(7)

# r = Aditya_return_Allpaths(root,7,0)
# print r

s = Solution()
result = s.pathSum(root,7)
print result

'''

#########################################################################################################

# Another Variation

# https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/
# Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent
# a number. Find the total sum of all root-to-leaf numbers % 1003.

#     1
#    / \
#   2   3

# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.

'''
# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treePathsSumUtil(root, val):
    # Base Case
    if root is None:
        return 0

    # Update val
    val = (val * 10 + root.val)
    print ("Value is %d") % (val)

    # If current node is leaf, return the current value of val - Aditya This will only retrun sum of specific path like 12 or 13
    if root.left is None and root.right is None:
        return val

    return (treePathsSumUtil(root.left,
                             val) +  # [Aditya] : Main function which Recur sum of values for left and right subtree. This will return 12+13 = 25
            treePathsSumUtil(root.right, val))


# @param A : root node of tree
# @return an integer
def sumNumbers(A):
    return treePathsSumUtil(A, 0) % 1003


#################################################

# Driver program to test above functions
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print ("\nSUM_RootToLeaf = %d") % (sumNumbers(root))

'''