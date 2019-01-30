
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate
# subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#
# The following are two duplicate subtrees:
#
#       2
#      /
#     4
#
# and
#
#     4
#
# Therefore, you need to return above trees' root in the form of a list.
# ================================================================================

# [Aditya]:
# Serialization of tree for every node, considering every node as root ( so we get
# serialised structure/string for each node, considering that node as root). So
# Serialization of root will be biggest and leaf node's smallest.

# Now after root, we proceed to left and right subtree and get their serialized structure
# considering them as root, and so on... So we keep doing Serialization for every node
# considering that node as root and then keep save the result in hash or counter.
# Now if hash or counter is two for any node's structure (serialised string), then they
# are duplicate subtree and append them to result.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dict = {}
        result = []

        def search(node):
            
            if not node:
                return "#"

            node_string = str(node.val) + search(node.left) + search(node.right)  # Serialization of that node 

            if node_string in dict:
                if dict[node_string] == 1:
                    result.append(node)
                    # To avoid duplicates
                    dict[node_string] = 2
            else:
                dict[node_string] = 1

            print node_string
            return node_string

        search(root)
        return result

"""
Your input

[1,2,3,4,null,2,4,null,null,4]

Your stdout

4##
24###
4##
24###
4##
324###4##
124###324###4##

Your answer

[[4],[2,4]]

Expected answer

[[4],[2,4]]

"""

    
    





