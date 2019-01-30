
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74379/Simple-and-intuitive-iterative-Python-solution-using-deque()-same-serialization-as-Leetcode-beats-95

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This code works for both LC-297 and LC-449.
class Codec:
    # Serialised using DFS (Recursive PreOrder traversal)
    def serialize(self, root):

        print "Serializing Tree into string :",
        def rserialize(root, string): # a recursive helper function for the serialize() function."""

            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        print rserialize(root, '') # Just for prining whole string
        return rserialize(root, '')



    # Decodes your encoded data to tree.
    def deserialize(self, data):

        print "Deserializing string into Tree: ",
        def rdeserialize(l):  # a recursive helper function for deserialization

            if l[0] == 'None':
                l.pop(0)
                return None # Just do nothing for string 'None' in serialised data. Simply return

            root = TreeNode(l[0])
            print root.val,         # To print values of tree.
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        return rdeserialize(data.split(','))


# =========================================================

# Output :

# Serializing Tree into string : 2,1,None,None,3,None,None,
# Deserializing string into Tree:  2 1 3





















from collections import deque

class Codec1:

    def serialize(self, root):
        string = ""
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                string += ",None"
                continue
            else:
                string += "," + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return string

    def deserialize(self, data):
        data = deque(data.split(","))
        _, val = data.popleft(), data.popleft()
        root = None if val == "None" else TreeNode(int(val))
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                a, b = data.popleft(), data.popleft()
                cur.left = TreeNode(int(a)) if a != "None" else None
                cur.right = TreeNode(int(b)) if b != "None" else None
                queue.append(cur.left)
                queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


