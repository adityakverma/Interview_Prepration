# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
#
#     4 -> 5 -> 1 -> 9
# Example 1:
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
#              should become 4 -> 1 -> 9 after calling your function.
# Example 2:
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
#              should become 4 -> 5 -> 9 after calling your function.
# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.
# # =================================================================================

class Solution(object):

    def deleteNode(self, node): # Do not return anything, modify node in-place instead.
        node.val, node.next = node.next.val, node.next.next

# When node is None or node is the last node, you should consider them
# separately. If the node is the last one, we have no other way except
# scanning from the beginning to the end, so the complexity is O(n),
# while this is the only case, other nodes can be done by replacing values,
# so the average complexity is still O(1). In Python, we don't need to
# contact with memory directly, the underlying memory manager will handle
# this for us. Here you can see the detailed description.

# Given the condition that head is not accessible from the method (verified in the
# leetcode code editor), it seems the only solution is to replace given node value
# with node.next.val and update node.next reference to node.next.next. Btw, similar
# question is discussed in Cracking the Coding Interview book.


