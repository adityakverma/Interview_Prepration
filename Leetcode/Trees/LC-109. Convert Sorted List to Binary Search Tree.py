
# Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order, convert
# it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in
# which the depth of the two subtrees of every node never differ by more than 1.
# ==================================================================================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # [Aditya]: Convert Linked List to list and then choose middle of list as root and
    # use slicing for making it to left and right tree

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next

        return self.treeFromList(l)

    def treeFromList(self, l):
        if not l:
            return

        if len(l) % 2 == 0:
            mid = len(l) / 2 - 1
        else:
            mid = len(l) / 2

        node = TreeNode(l[mid])
        node.left = self.treeFromList(l[:mid])
        node.right = self.treeFromList(l[mid + 1:])

        return node

    ################################################################################

    # Solution based on finding middle of Linked list using two pointers and then making
    # middle as root. And then make tree - left subtree from head to middle and right
    # subtree from middle to end of linked list.
    # Python recursive solution with detailed comments (operate linked-list directly).
    # [IMP]: BUT Should we still retain the linkedlist ? Should we not to use extra O(n) space ?

    def sortedListToBST_(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # tmp points to node after mid, since slow will be at middle
        tmp = slow.next
        # cut down the left child
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root

        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2',
        # '3' is root,'12' belongs to left, '45' belongs to right

    ################################################################################




