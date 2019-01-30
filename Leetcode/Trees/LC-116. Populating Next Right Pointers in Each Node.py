
# Given a binary tree

# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
#
# Populate each next pointer to point to its next right node. If there is no next right
# node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
#     You may only use constant extra space.
#     Recursive approach is fine, implicit stack space does not count as extra space for
#     this problem.
#     You may assume that it is a perfect binary tree (ie, all leaves are at the same level,
#     and every parent has two children).
#
# Example:
#
# Given the following perfect binary tree,
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
#
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL
# ---------------------------------------------------------------------------------------------

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing


    def connect(self, root): # ACCEPTED

        if root is None:
            return

        if root.left:  # Idea is : Connect both children of this root. And right child of itself with neighbour's left child.
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

    # ===================================================

    def helper(self, left, right):

        if not left or not right:
            return

        left.next = right
        self.helper(left.right, right.left)
        self.helper(left.left, left.right)
        self.helper(right.left, right.right)

    def connect_(self, root):
        if not root:
            return

        self.helper(root.left, root.right)

    # ===============================================

if __name__ == '__main__':

    s = Solution()

    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.left.right.left = TreeLinkNode(8)

    s.connect(root)

# Explanation
# Since each node is guaranteed to have both left and right child, we know:
#
#     Left child should always point to right child
#     Right child should always point to parent's neighbor's left child.
#     If neighbor is None, it means current node is the right most neighbor of the level, and right child should point to None as well.
#
# For example,
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
#
# For node 2,
#
#     4 will point to 5
#     5 will point to 2's neighbor, 3's left child, which is 6
#     7 will point to None since 3 is pointing to None as well



'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    
    def connect(self, root):
        cur = root
        if not cur:
            return root
            
        count = 1
        prev_nodes = [cur]
        cur_nodes = []
        flag = 0
        
        while True:
            for node in prev_nodes:
                if node.left and node.right:
                    cur_nodes.append(node.left)
                    cur_nodes.append(node.right)
                else:
                    flag = 1
                    break
            if flag:
                break
                
            for i in range(len(cur_nodes) - 1):
                cur_nodes[i].next = cur_nodes[i+1]
            prev_nodes = cur_nodes
            cur_nodes = []
        #return root

'''