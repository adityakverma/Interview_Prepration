
#  A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.

# Return a deep copy of the list.
# ==========================================================================

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    # Copying List means creating new node for each unseen nodes and link them.
    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node with the label same as old node. Copying List means creating new node for each unseen nodes and link them.
        node = RandomListNode(head.label)
        # Save this value in the hash map. This is needed since there might be loops during traversal due to random pointers.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls. Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

