
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# A node structure
class TreeNode:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution():    # Best question - understood all solutions Recusrion and Iterative.

    def rightSideView(self,root):
        return self.rightSideView1(root)

    #---------------------------------------------

    # Level Order Traversal with Right side recursion first
    def rightSideView1(self, root): # Level Order where we call Right side first for recursion
        res = []
        self.levelOrder(root, 0, res)
        return res

    def levelOrder(self, node, level, res):
        if node:
            if len(res) == level:
                res.append(node.val) # # Just append for first value from right for each level - others get ignored

            self.levelOrder(node.right, level + 1, res) # Right first so we get Right side view
            self.levelOrder(node.left, level + 1, res)

    # ----------------------------------------------

    # # Level Order Traversal with Left side recursion first
    def LeftSideView(self, root):  # Level Order where we call left side first for recursion
        res = []
        self.levelOrder(root, 0, res)
        return res

    def L_levelOrder(self, node, level, res):
        if node:
            if len(res) == level:
                res.append(node.val)  # Just append for first value from left for each level - others get ignored

            self.L_levelOrder(node.left, level + 1, res) # Left side first to get left side view
            self.L_levelOrder(node.right, level + 1, res)

    #==============================================
    # DFS + stack
    def rightSideView2(self, root):  # UNDERSTOOD - Same as above except use of stack
        res, stack = [], [(root, 0)]    # This is same as above except passing of value during call - instead we are using stack concept
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                stack.append((curr.left, level + 1)) # Doing left first as pop() gives right most value first
                stack.append((curr.right, level + 1))
        return res

    #---------------------------------------------
    # BFS + queue
    def rightSideView3(self, root):  # UNDERSTOOD - Same as above
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                queue.append((curr.right, level + 1)) # Doing Right first as popping from front - queue.pop(0)
                queue.append((curr.left, level + 1))
        return res

    #---------------------------------------------
    res = []
    def rightSideView_Aditya(self, root):  # Works but not for all case
        if root is None:
            return
        self.res.append(root.val)
        if root.right:
            self.rightSideView_Aditya(root.right)
        return self.res
    #---------------------------------------------


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.right.left = TreeNode(7)

    print s.rightSideView(root)

# ----------------------------------------------------------------------

# https://leetcode.com/problems/binary-tree-right-side-view/discuss/170379/Simple-Iterative-BFS-and-DFS-in-python

