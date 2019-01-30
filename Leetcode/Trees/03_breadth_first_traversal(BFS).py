
class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

# Also try LC-199. Same logic
class Solution(object):

    # ------------ BFS using Queue ---------------------------------
    def BFS_Iterative(self, root):          # LC-102

        if not root:
            return

        res = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)   # Try to change this to pop() and see magic. Also either you call this stack or queue

            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))    # Starts with left side first
            if node.right is not None:
                queue.append((node.right, level + 1))   # then right side

        return res

    # ----------------------------------------------------------
    def BFSLevels_Iterative(self, root):

        res = []
        if not root:
            return res
        queue = [root]

        while queue:
            total, cnt = 0, len(queue)

            for _ in xrange(cnt):
                node = queue.pop(0)
                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    # ----------------------------------------------------------
    def BFS_Recursive(self, root):
        result = []
        self.level_bfs(root, 0, result)
        return result

    def level_bfs(self, node, level, result):

        if not node:
            return

        if level == len(result):
            #print len(result), level, result
            result.append([]) # when new level starts, then put new [] brackets
        result[level].append(node.val)
        #print len(result), level, result

        self.level_bfs(node.left, level + 1, result)  # Starts with left side first
        self.level_bfs(node.right, level + 1, result) # Once done with all left subtree then we goto right side, where we add node 3



if __name__ == '__main__':

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(8)

    print "\nLevel order Recursive is :\n", s.BFS_Recursive(root)
    print "\nLevel order Iterative is :\n", s.BFS_Iterative(root)
    print "\nLevel order Iterative is :\n", s.BFSLevels_Iterative(root)

# Try : https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
