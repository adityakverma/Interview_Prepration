
# Merge k sorted linked lists and return it as one sorted list. Analyze
# and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# -----------------------------------------------------------------
# Idea: Assuming K number of linkedlists, and N number of elements
# Initialize the heap. In Python this is just a list. We need K tuples.
# One for the index for which linkedlist node among the list of linked
# lists the element lives; the value of the element and the node itself.
# Since we want the key of the heap to be based on the value of the element,
# we should put that first in the tuple.
#
# While the heap is not empty we need to:
# Extract the minimum element from the heap: (value, list index, list node)
# If the list node is not the last node, add the next tuple in the list index.

# ------------------------------------------------------------------
# **Complexity Analysis: **
#
# Time - O(KN log K)
# *While loop runs for K N times while heapq operations(push and pop takes log K time) *
#
# Space - O(K)
# *Heap will have a maximum of K elements at any point of time *

# Note: Aditya, if here lists were not sorted then heap solution would have not been
# possible because we cannot maintain heap of N nodes ( where N is sum of all nodes
# of all lists). Here we're just maintaining heap of size K (3) because lists are sorted
# and we know once we pop from any list then we can push next element from that list
# itself.
# ---------------------------------------------------------------------

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):

    # https://leetcode.com/problems/merge-k-sorted-lists/discuss/180757/Using-priority-queue-with-explanation-python

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head, tail = None, None
        heap = [(node.val, node) for node in lists if node]
        heapq.heapify(heap)
        #print heap

        while heap:
            node_val, node = heapq.heappop(heap)
            #print heap

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

            if not head:
                head, tail = node, node
            else:
                tail.next = node
                tail = node

        return head

    ############################################################################


    def mergeKLists__(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next

    ################################################################################

    # Merge Sort

    def mergeKLists_(self, lists):
        if not lists:
            return None
        start = 0
        end = len(lists) - 1
        while start != end or end != 0:
            if start >= end:
                start = 0
            else:
                lists[start] = self.mergeTwoLists(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        current = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return head.next

    ###################################################################################

if __name__ == '__main__':

    # Input = [
    #        1->4->5,
    #        1->3->4,
    #        2->6
    #    ]

    inputLists = [[1,4,5],[1,3,4],[2,6]]

    s = Solution()

    #print s.mergeKLists(inputLists)






