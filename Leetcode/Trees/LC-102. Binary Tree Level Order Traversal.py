
# FB, MS, AWS, Apple, LinkedIn, BFS
# Below is good solution but it fails for below input below where left subtree is smaller than right

# Given Input:  [3,9,20,null,null,15,7]
# Expected Answer: [[3],[9,20],[15,7]]

class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

# Also try LC-199. Same logic
class Solution(object):

    # ----------------------------------------------------------
    def levelOrder(self, root):
        result = []
        self.level_dfs(root, 0, result)
        return result

    def level_dfs(self, node, level, result):
        if not node:
            return

        if level == len(result):
            result.append([]) # when new level starts, then put new [] brackets
        result[level].append(node.val)

        self.level_dfs(node.left, level + 1, result)  # Starts with left side first
        self.level_dfs(node.right, level + 1, result) # then right side

    # ----------------------------------------------------------
    def levelOrder_Iterative(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop(0)   # Try to change this to pop() and see magic. Also either you call this stack or queue

            if curr:
                if len(res) == level:
                    res.append([])
                res[level].append(curr.val)

                stack.append((curr.left, level + 1))    # Starts with left side first
                stack.append((curr.right, level + 1))   # then right side

        return res

if __name__ == '__main__':

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)

    print "\nLevel order traversal of BT is :\n", s.levelOrder(root)
    print "\nLevel order traversal of BT is :\n", s.levelOrder_Iterative(root)



# Try : https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/


























'''
# =====================================ACCEPTED ===============================

# Stack based
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution5(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # list in a list
        result = []
        if not root:
            return result

        curr_level = [root]
        while curr_level:
            # append each level to curr_level
            result.append([node.val for node in curr_level])

            # check if each node in curr_level have children
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
        return result

# ==================================== ACCEPTED ==============================

from collections import deque
class Solution1:

    def levelOrder(self, root):
        if not root: return []
        traversal_queue = deque([root])
        ans = []
        while traversal_queue:
            level_len = len(traversal_queue)
            level_nodes = []
            while level_len > 0:
                node = traversal_queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    traversal_queue.append(node.left)
                if node.right:
                    traversal_queue.append(node.right)
                level_len -= 1
            ans.append(level_nodes)
        return ans

# =====================================ACCEPTED ===============================


# Python BFS with queue, easy to understand
class Solution4(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            nextQueue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)

                if node.right:
                    nextQueue.append(node.right)

            queue = nextQueue
            res.append(level)
        return res
'''
# ===========================================================================
