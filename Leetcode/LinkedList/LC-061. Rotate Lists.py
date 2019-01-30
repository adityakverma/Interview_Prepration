# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        pp = head
        count = 0
        while pp:
            pp = pp.next
            count += 1
        for i in range((k % count)):
            head = self.rotate(head)
        return head

    def rotate(self, head):
        p = head
        pre = None
        while head.next:
            pre, head = head, head.next
        head.next = p
        pre.next = None
        return head