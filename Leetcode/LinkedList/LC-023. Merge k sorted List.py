
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeKLists(self, lists):

        totalLists = len(lists)
        interval = 1
        while interval < totalLists:

            for i in range(0, totalLists - interval, interval * 2):    # 1st combine l0,l1 making new l0; then l2,l3 making new l2, so on..
                lists[i] = self.mergeTwoList(lists[i], lists[i + interval])

            interval *= 2   # Then combine new l0 and new l2 and so on..
        return lists[0] if totalLists > 0 else lists

    def mergeTwoList(self, l1, l2):

        if not l1: return l2
        if not l2: return l1

        curr = head = ListNode(0)  # <== using Dummy node and then return dummy.next
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return head.next

    # Space complexity : O(1)
    # Time complexity : O(N log k) where k is the number of linked lists.
    # ----------------------------------

    # Method-02.
    def mergeKLists_(self, lists):

        self.nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val) # Traverse all LL and store values to array.
                l = l.next

        for x in sorted(self.nodes): # Sort and iterate over this array to get the proper value of nodes.
            point.next = ListNode(x) # Create a new sorted linked list and extend it with the new nodes.
            point = point.next

        return head.next

# -------------------------------------------------------------------------