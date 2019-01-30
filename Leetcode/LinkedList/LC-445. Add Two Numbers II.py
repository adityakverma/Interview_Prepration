
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# ----------------------------------------------------------------------------
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry, tail = 0, None
        while stack1 or stack2 or carry:
            v1 = v2 = 0
            if stack1:
                v1 = stack1.pop()  # This is good option to pop from stacks, instead of reversing the Linkedlist
            if stack2:
                v2 = stack2.pop()
            carry, value = divmod(v1 + v2 + carry, 10)

            node = ListNode(value)
            node.next = tail  # We keep growing from right to left, so tail is updated.
            tail = node

        return node



