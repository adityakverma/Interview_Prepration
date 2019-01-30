
# Python program to perform iterative preorder traversal

# A binary tree node
class TreeNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#  Pop all items one by one. Do following for every popped item
#   a) print it
#   b) push its right child
#   c) push its left child
# Note that right child is pushed first so that left
# is processed first */

class Solution():
    # An iterative process to print preorder traveral of BT
    def iterativePreorder(self,root):
        # Base Case
        if root is None:
            return

        result = []
        stack = []
        stack.append(root) # We append because we want root first in preOrder

        while(stack):

            # Pop the top item from stack and print it
            node = stack.pop()
            result.append(node.data)

            # Push right and left children of the popped node to stack
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result


# Driver program to test above function
if __name__ == '__main__':

    s = Solution()
    # Driver code
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print "\nIterative PreOrder :",s.iterativePreorder(root)

