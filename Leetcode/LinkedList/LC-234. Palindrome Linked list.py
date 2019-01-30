
# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true
# --------------------------------------------------------------

# Time Complexity : O(N)
# Space Complexity: O(1), since he changes the linked list nodes in place.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def isPalindrome(self, head):

        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        prev = None
        while slow:  # Slow now points to midpoint or head of 2nd half
            nxt = slow.next
            slow.next = prev  # Link backwards

            prev = slow # Move pointers ahead
            slow = nxt  # Move pointers ahead

        # compare the first and second half nodes. Note: here prev is head of 2nd half of LL which was just reversed.
        while head and prev:  #
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
# --------------------------------------------------------
# But here Space complexity is not O(1). Instead its O(N)
def isPalindrome(self, head):
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]

# --------------------------------------------------------

def isPalindrome_(self, head):
    # bound consideration
    if not head or not head.next:
        return True

    # find the head of the second half part
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # slow now is the head of second half

    # reverse the second half
    prev = None
    while slow:
        slow.next, slow, prev = prev, slow.next, slow
    # prev now is the head of reversed second half

    # compare the first part and the second part
    first = head
    second = prev
    while first and second:
        if first.val != second.val:
            return False
        first, second = first.next, second.next
    return True


