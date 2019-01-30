
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        depth = float('inf')

        if root is None:
            return 0
        else:
            queue.append((1, root)) # Note in all these depth question we insert levels also. Just like BFS traversal.

        while queue:
            level, node = queue.pop(0)

            if not any((node.left, node.right)): # Only find depth if reached to end (leaf)
                depth = min(depth, level)        # Note: We use min function

            if node.left is not None:            # else keep increasing level and move downwards until we reach leaf.
                queue.append(( level +1, node.left))
            if node.right is not None:
                queue.append(( level +1, node.right))

        return depth

        # ----------------------------------------------------------------------------------
        # BFS Iteration using Queue
        #
        # The drawback of the DFS approach in this case is that all nodes should be visited
        # to ensure that the minimum depth would be found. Therefore, this results in a
        # O(N) complexity. One way to optimize the complexity is to use
        # the BFS strategy. We iterate the tree level by level, and the first leaf we reach
        #  corresponds to the minimum depth. As a result, we do not need to iterate all nodes.
        # ----------------------------------------------------------------------------------


