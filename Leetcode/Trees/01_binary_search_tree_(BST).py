# Python program to demonstrate insert operation in binary search tree
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.geeksforgeeks.org/binary-search-tree-data-structure/

# A utility class that represents an individual node in a BST
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution():

    # --------------------------------------------------
    # A utility function to insert a new node with the given key
    def insert(self,root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
    # --------------------------------------------------
    # A utility function to search a given key in BST
    def search(self,root, key):

        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            print ("Search: Found %d") %(key)
            return root

        # Key is greater than root's key
        if root.val < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)
    # --------------------------------------------------
    # A utility function to do inorder tree traversal
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    # --------------------------------------------------

# Driver program to test the above functions
# Let us create the following BST
#      50
#    /   \
#   30   70
#  / \   / \
# 20 40 60 80

if __name__ == '__main__':

    s = Solution()

    r = TreeNode(50)
    s.insert(r, TreeNode(30))
    s.insert(r, TreeNode(20))
    s.insert(r, TreeNode(40))
    s.insert(r, TreeNode(70))
    s.insert(r, TreeNode(60))
    s.insert(r, TreeNode(80))

    # Print inoder traversal of the BST
    print s.inorder(r)
    print s.search(r,60)

