
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from
# the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
#
# Example:

#      1
#    /   \
#   2     3
#  / \
# 4  5

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:

    # ==================================================
    # DFS Recursive

    def maxDepth(self, root):   # DFS Recursion (PreOrder) w/ levels which helps to track Depth of tree. Looks like BFS, but its DFS w/ levels
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0

        def dfs(node,level):

            if root is None:    # This is exit condition for all recursive calls to return.
                return 0

            if not node.left or not node.right:                  # Meaning if we have reached to end (leaf), then only find max depth
                self.max_depth = max(self.max_depth, level + 1)  # Note: We use max function

            if node.left is not None:
                dfs(node.left, level + 1)
            if node.right is not None:
                dfs(node.right, level + 1)

        dfs(root,0)
        return self.max_depth

    # -----------------------------------------------
    # DFS using stack

    def maxDepth_Iterative_DFS(self, root):

        if root is None:
            return 0

        stack = []
        max_depth = 0
        stack.append((1, root))  # Note in all these depth question we insert levels also. Just like BFS traversal.

        while stack:
            current_depth, node = stack.pop()

            if not node.left or not node.right:  # Meaning if we have reached to end, then only find max depth, else keep calling recurisve function and add levels.
                max_depth = max(max_depth, current_depth)  # Note: We use max function

            if node.left is not None:
                stack.append((current_depth + 1, node.left))
            if node.right is not None:
                stack.append((current_depth + 1, node.right))

        return max_depth

    # -----------------------------------------------old -----

    def maxDepth_(self, root): # LC-104

        if root is None:
            #print "Now return 0, since we reached end.."
            return 0     # This is exit condition for all recursive calls to return. Ofcourse this is also initial condition to check.
        else:
            left_height = self.maxDepth_(root.left) # First time it reaches all the way to node 4 in bottom and returns 0, then it keeps adding 1 and returns other prior recursive calls made.
            #print "\nLeft", left_height, root.val

            right_height = self.maxDepth_(root.right)
            #print "right", right_height, root.val

        #print "Now RETURN........................"
        return max(left_height, right_height) + 1      # Note: We use max function
        #return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


    # -----------------------------------------------
    # BFS using stack

    def maxDepth_Iterative_BFS(self, root):

        queue = []
        max_depth = 0

        if root is None:
            return 0
        else:
            queue.append((1, root))  # Note in all these depth question we insert levels also. Just like BFS traversal.

        while queue:
            current_depth, node = queue.pop(0)

            if not node.left or not node.right:
                max_depth = max(max_depth, current_depth) # Note: We use max function

            if node.left is not None:
                queue.append((current_depth + 1, node.left))
            if node.right is not None:
                queue.append((current_depth + 1, node.right))

        return max_depth

    #####################################################################################################################
    #####################################################################################################################
    #####################################################################################################################




    def minDepth(self, root): # LC-111

        if root is None:
            return 0
        else:
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)

        return min(left_height, right_height) + 1  # Note: We use min function.

    # -----------------------------------------------
    # DFS using Queue
    def minDepth_Iterative_DFS(self, root):

        stack = []
        depth = float('inf')

        if root is None:
            return 0
        else:
            stack.append((1,root))

        while stack:
            level, node = stack.pop()

            if not any((node.left, node.right)):
                depth = min(depth, level)       # Note: We use min function

            if node.left is not None:
                stack.append((level+1, node.left))
            if node.right is not None:
                stack.append((level+1, node.right))

        return depth

    # Time Complexity: O(N)
    # Space Complexity: O(N)

    # --------------------------------------------------------

    # BFS Iteration using Queue
    #
    # The drawback of the DFS approach in this case is that all nodes should be visited
    # to ensure that the minimum depth would be found. Therefore, this results in a
    # O(N) complexity. One way to optimize the complexity is to use
    # the BFS strategy. We iterate the tree level by level, and the first leaf we reach
    #  corresponds to the minimum depth. As a result, we do not need to iterate all nodes.


    def minDepth_Iterative_BFS(self, root):

        queue = []
        depth = float('inf')

        if root is None:
            return 0
        else:
            queue.append((1, root))  # Note in all these depth question we insert levels also. Just like BFS traversal.

        while queue:
            level, node = queue.pop(0)

            if not any((node.left, node.right)):  # Only find depth if reached to end (leaf)
                depth = min(depth, level)  # Note: We use min function

            if node.left is not None:  # else keep increasing level and move downwards until we reach leaf.
                queue.append((level + 1, node.left))
            if node.right is not None:
                queue.append((level + 1, node.right))

        return depth

    # ========================================================

    def treeSize(self,node):
        if node is None:    # This is super important condition. This is how all recursive calls made will return. Definately this also checks initial condition too.
            return 0
        else:
            tree_Size = self.treeSize(node.left) + 1 + self.treeSize(node.right)
        return (tree_Size)

    # -----------------------------------------------

#      1
#    /   \
#   2     3
#  / \
# 4  5

if __name__ == '__main__':
    s =  Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print "\n-------------------------"
    print "\n Max Depth (Recursion):",s.maxDepth(root)
    print "\n Max Depth (Iterative) BFS:",s.maxDepth_Iterative_BFS(root)
    print "\n Max Depth (Iterative) DFS:",s.maxDepth_Iterative_DFS(root)

    print "\n-------------------------"
    print "\n Min Depth (Recursion):",s.minDepth(root)
    print "\n Min Depth (Iterative) BFS:",s.minDepth_Iterative_BFS(root)
    print "\n Min Depth (Iterative) DFS:",s.minDepth_Iterative_DFS(root)

    print "\n-------------------------"
    print "\n Tree Size:", s.treeSize(root)
    print "\n-------------------------"




