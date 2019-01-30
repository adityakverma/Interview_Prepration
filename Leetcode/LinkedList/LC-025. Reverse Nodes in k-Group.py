
# Given a linked list, reverse the nodes of a linked list k at a time and return
# its modified list.
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in the
# end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#     Only constant extra memory is allowed.
#     You may not alter the values in the list's nodes, only nodes itself may be changed.

# ----------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/145203/Easy-to-Understand-Python-Solution-with-Comments

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # sentinel makes it so that we can cleanly pass curr.next into reverseK,
        # which we want to do because we want to update curr.next to the next
        # group's new head
        sentinel = ListNode(0)
        sentinel.next = head
        curr = sentinel

        # we calculate how many groups or blocks are in the linked list
        length = 0
        while curr.next is not None:
            curr = curr.next
            length += 1
        blocks = length/k

        # we go through the list and reverse groups of size k
        curr = sentinel
        counter = 0
        while curr is not None and blocks > 0:
            if counter % k == 0:
                curr.next = self.reverseK(curr.next, k)
                blocks -= 1
            curr = curr.next
            counter += 1
        return sentinel.next


    def reverseK(self, head, k):
        """Reverse a group of k nodes with 2 pointers, one behind the other, by flipping links"""
        i = 0
        prev = None
        curr = head
        while i < k:

            tail = curr.next
            curr.next = prev # Flip pointer

            prev = curr
            curr = tail
            i += 1
        # head is now the tail of the reversed group, so we set its next to the start of the next group
        head.next = tail
        # return the head of the reversed group, which was the tail of the original group
        return prev


# ------------------------------------------------------------------------------------------

# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11425/Simple-Python-solution-one-pass-no-additional-space-109ms

# The key idea is to keep track of the next_head while reversing the group,
# tail of the current group is always the start node of the group, once the
# group reversing is done, next_head is available, simply connect it to tail.


def reverseKGroup(self, head, k):
    if head is None or k < 2:
        return head

    next_head = head
    for i in range(k - 1):
        next_head = next_head.next
        if next_head is None:
            return head
    ret = next_head

    current = head
    while next_head:
        tail = current
        prev = None
        for i in range(k):
            if next_head:
                next_head = next_head.next
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        tail.next = next_head or current

    return ret

