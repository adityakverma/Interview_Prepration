
# Python program for iterative postorder traversal using
# two stacks

# So, we can do something like iterative preorder traversal with the following differences:
# a) Instead of printing an item, we push it to a stack.
# b) We push the left subtree before the right subtree.

# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# An iterative function to do postorder traversal of a given binary tree
class Solution():

    def postorderTraversal_LC145(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        ret, stack = [], [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            ret.insert(0, node.data)

        print ret
        return ret

    # ----------------------------------------------
    def postOrderIterative(self,root):

        if root is None:
            return

        # Create two stacks
        s1 = []
        s2 = []

        s1.append(root)

        # Run while first stack is not empty
        while s1:
            # Pop an item from s1 and append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of removed item to s1
            if node.left is not None:
                s1.append(node.left)
            if node.right is not None:
                s1.append(node.right)

        # Print all elements of second stack
        while s2:
            node = s2.pop()
            print node.data,

    # Driver program to test above function
if __name__ == '__main__':
    s = Solution()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    s.postorderTraversal_LC145(root)


    s.postOrderIterative(root)
