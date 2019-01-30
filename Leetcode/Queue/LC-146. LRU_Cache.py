

#

################################ ACCEPTED ###########################################

import collections

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self._cash = collections.OrderedDict()

    def get(self, key):
        cash = self._cash

        # Case when dictionary doesn't contain key
        if key not in cash:
            return -1

        # Case when dictionary contains key: the order of items should be updated.
        cash.move_to_end(key) # Runs ONLY on Python 3 compiler

        return cash[key]


    def put(self, key, value):
        cash = self._cash

        # Case when key-value pair is already stored and should be updated
        if key in cash:
            del cash[key]
            cash[key] = value
            return

        # Case when key-value pair is totally new
        cash[key] = value
        if len(cash) > self.capacity:
            cash.popitem(last=False)

# Smart choice to use OrderedDict !
# Note: move_to_end() only exists in Python 3 (After Python 3.2)

################################ ACCEPTED ###########################################

class LRUCache_(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.queue = [None] * capacity
        self.dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            # update value
            self.queue.remove(key)
            self.queue.append(key)
            self.dict[key] = value
            return
        else:
            # add value
            if None not in self.queue:
                del self.dict[self.queue[0]]
            self.queue.pop(0)
            self.queue.append(key)
            self.dict[key] = value

#####################################################################################

# https://leetcode.com/problems/lru-cache/discuss/187924/python:-O(1)-dict-+-double-linked-list-and-O(k)-dict-+-heap

# Is there a specific reason for using doubly linked list instead of, say an array of a deque? I was thinking that if it's only for keeping the order, all three of them should be fine. Am I misunderstanding something, or is there an advantage in performance for doubly linked list?
# es. Moving an element in an array or deque costs O(N) time (since all elems before/after the moved element need to be shifted).
#
# Moving an element in a doubly linked list is O(1) time, since there is a constant number of pointers we need to update for the move (only the prev/next pointers of the moved element, the prev/next pointers of neighbors at its current position, and the prev/next pointers of neighbors at its destination)
#
# In this solution, we constantly need to move elements around in this data structure, so to optimize for time complexity we use a doubly linked list.

# @by6 but doesn't moving an element in a doubly linked list really cost O(n) time, because you have to follow each link to find the nth item?
# @dmzDhYqRVkZAr4dj we actually get the node via the dictionary in O(1), not follow the link.

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache_:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

