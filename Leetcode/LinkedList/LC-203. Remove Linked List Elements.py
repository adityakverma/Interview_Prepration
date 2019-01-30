
# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# ========================================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head is not None and head.val == val:
            head = head.next

        current = head
        while current is not None:
            if current.next is not None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# First we remove all (if any) target nodes from the beginning (we do it because the
# removing logic is slightly different from when the node is not in the head). After
# that we just loop over all nodes, if the next one is one that should be removed, just
# get it out of the list by moving the next pointer to the next-next node. Otherwise
# just move along the list.


