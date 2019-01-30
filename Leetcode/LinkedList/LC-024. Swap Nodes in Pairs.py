
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Note:
#
#     Your algorithm should use only constant extra space.
#     You may not modify the values in the list's nodes, only nodes itself may
#     be changed.
# =========================================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def swapPairs(self, head):

        res = prev = ListNode(0)
        res.next = head

        while head and head.next:
            tmp = head.next

            prev.next = tmp  # step a
            head.next = tmp.next  # step b
            tmp.next = head  # step c

            prev = head
            head = head.next

        return res.next

    # Please see the image we saved for this.

    # ============================================
    def swapPairs_Mapara(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next: return head

        prev = ListNode(0)
        newHead = head.next  # Store the starting node for returning purpose

        while head and head.next:

            first = head
            second = head.next
            temp = second.next

            if (prev is not None):
                prev.next = second

            second.next = first
            first.next = temp

            prev = first
            head = temp

        return newHead

#################################################################################

# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode-tm


