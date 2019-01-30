
# Python program to do inorder traversal without recursion

# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution():

    def inorderTraversal(self, root):

        res, stack = [], []
        while stack or root :
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.data)
                root = root.right
        return res

if __name__ == '__main__':
    s = Solution()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print "\nIterative InOder: ",
    print s.inorderTraversal(root)


""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
