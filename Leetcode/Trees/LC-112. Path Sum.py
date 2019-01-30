
# Given a binary tree and a sum, determine if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def hasPathSum(self, node, sum):
        if node == None:
            return False

        if node.left is None and node.right is None and node.val == sum: # IMP - Checking for leaf : When reached here, verify the sum
            return True

        # we should return True if either the left subtree or the right subtree has correct path sum.
        return self.hasPathSum(node.left, sum - node.val) or self.hasPathSum(node.right, sum - node.val)

    # ---------------------------------------------------
    # DFS with stack
    def hasPathSum_iterative_stack(self, root, sum):

        if not root:
            return False
        stack = [(root, root.val)]

        while stack:
            curr, val = stack.pop()  # Since Stack is LIFO, so popping first item.
            if not curr.left and not curr.right and val == sum:
                return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False

    # ---------------------------------------------------
    # BFS with queue
    def hasPathSum_iterative_queue(self, root, sum):
        if not root:
            return False
        queue = [(root, sum - root.val)]
        while queue:
            curr, val = queue.pop(0) # Since Queue is FIFO, so popping first item.
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False
    # ---------------------------------------------------

if __name__ == '__main__':

    s = Solution()

    root = TreeNode(1)
    root.left  = TreeNode(2)
    root.left.left  = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    check_sum = 10

    if s.hasPathSum(root,check_sum):
        print("\nYES. SumPath is present")
    else:
        print("\nNO. SumPath not Present")

    if s.hasPathSum_iterative_stack(root,check_sum):
        print("\nYES. SumPath is present")
    else:
        print("\nNO. SumPath not Present")

    if s.hasPathSum_iterative_queue(root,check_sum):
        print("\nYES. SumPath is present")
    else:
        print("\nNO. SumPath not Present")

