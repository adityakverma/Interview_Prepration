
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single 
# digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 
# 0 itself.
# 
# Example:
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# ----------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret
        add = 0

        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add


            cur.next = ListNode( val % 10)            # Just started with first value addition from here, where we create first node for added value.
            add = val / 10
            # print "First", cur.val, cur.next.val    # So in case of 6+4, where make listnode of 0 ( as 10%10=0 ) and add=1 (10/10=1), which
                                                      # is added with next value i.e. 3+4+1=8
            cur = cur.next
            # print "Next",cur.val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ret.next



