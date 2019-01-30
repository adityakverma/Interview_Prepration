
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

###########################################################################################

class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

class Solution():

    # -----------------------------------------------------
    # We can solve this problem by using BFS with queue. Level information is needed
    # in order to reverse the odd row.

    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) == level :
                res.append([])

            if level % 2 == 0:
                res[level].append(root.val) # Add to last - meaning Append
            else:
                res[level].insert(0, root.val) # Add to front - insert(0,root.val)

            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

    # -----------------------------------------------------
    # dfs + stack
    def zigzagLevelOrder_(self, root):
        # write your code here
        res, stack = [], [(root, 0)]
        while stack:
            cur, level = stack.pop()
            if cur:
                if len(res) == level :
                    res.append([])

                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)

                stack.append((cur.right, level + 1))
                stack.append((cur.left, level + 1))
        return res

    # -----------------------------------------------------


if __name__ == '__main__':

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    #root.left.right.left = TreeNode(8)

    print "\nLevel order traversal of BT is :\n", s.zigzagLevelOrder(root)
    print "\nLevel order traversal of BT is :\n", s.zigzagLevelOrder_(root)

    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/34115/Python-short-iterative-solution-with-explanation.
    
# -----------------------------------------------------


'''
def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    queue = [root]
    res = []
    level = 0
    
    while queue:
        level += 1
        temp = []
        tempq = []
        
        for node in queue:
            temp.append(node.val)
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
        queue = tempq
        if level % 2 == 0 :
            temp = temp[::-1]
        res.append(temp)
        
    return res
    
# It's simple BFS version of tree traversal, only difference if that when level is odd, just simply reverse the value list in this level. Hope it helps.
    
'''