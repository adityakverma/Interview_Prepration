
# https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/Python-O(-N-)-solution.-easy-to-understand

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        print "values" ,vals

        return ' '.join(map(str, vals))


    # O( N ) since each val run build once
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print "data", data
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))


 # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# ==================================================================

# This is a great solution, but it is not O(N) because you pop(0) in the build() function.
# Every pop(0) is already O(N) and this operation is applied to all nodes. Instead, you
# can use deque() for the list vals.


# ===================================================================
# Now that I've actually read and solved this problem: The difference is the bold "The encoded
# string should be as compact as possible" here. The special property of binary search trees
# compared to general binary trees allows a more compact encoding. So while the solutions to
# problem #297 still work here as well, they're not as good as they should be.

# The main difference is as compact as possible.
# For BST, a simple pre-order or post-order traversal is enough to construct a BST tree.
# You might wonder why pre-order/post-order? why not in-order? See here for details
# https://stackoverflow.com/a/12880809/5684889

# I've just copy pasted #297's code and got accepted.
#  Every BST is a BT, so how would a BT (297) solution fail for BSTs (this one)?
# A solution for BST could fail BT, not the other way around


