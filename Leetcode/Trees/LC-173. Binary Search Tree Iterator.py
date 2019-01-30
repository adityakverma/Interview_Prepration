
# This is Inorder traversal of BST which will give elements in ascending order.
# But don't use recursion because then every time it will start from root to fetch
# next element). Instead here we use iterative approach for Inorder traversal

# Implement an iterator over a binary search tree (BST). Your iterator will
# be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Definition for a  binary tree node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class BSTIterator:  # Accepted

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q=[]
        self.allLeftIntoStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        self.allLeftIntoStack(cur.right)
        return cur.val

    def allLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# Aditya :

# Space Complexity is O(log N) where N is number of nodes so atlernate answer
# is depth of tree. Because this stack will never go beyond size of depth of
# tree due to constant pop and push.

# Time complexity : the average time complexity is O(1), you can see, somtimes
# node.right even can be None. As the total number of nodes in a tree is n, so
# the number of node.right can't be larger than n, and next() can be called n times,
# so the amortized time complexity is O(1).

