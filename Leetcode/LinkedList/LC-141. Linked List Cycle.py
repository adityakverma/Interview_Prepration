
# 141. Linked List Cycle
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# ========================================================================================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def hasCycle(self, head):

        slow = fast = head

        while fast and fast.next:  # This way we do not need to check if head is null.

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False

#
#     Use two pointers, walker and runner.
#     walker moves step by step. runner moves two steps at time.
#     if the Linked List has a cycle walker and runner will meet at some
#     point.
# ========================================================================================

