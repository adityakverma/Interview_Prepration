
# Python program to for tree traversals
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/


# A class that represents an individual node in a
# Binary Tree
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution():

    # A function to do inorder tree traversal
    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print(root.val),
            self.printInorder(root.right)


    # A function to do postorder tree traversal
    def printPostorder(self,root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.val),


    # A function to do postorder tree traversal
    def printPreorder(self,root):
        if root:
            print(root.val),
            self.printPreorder(root.left)
            self.printPreorder(root.right)

if __name__ == '__main__':

    s = Solution()
    # Driver code
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print "\nPreorder traversal of binary tree is"
    s.printPreorder(root)

    print "\nInorder traversal of binary tree is"
    s.printInorder(root)

    print "\nPostorder traversal of binary tree is"
    s.printPostorder(root)