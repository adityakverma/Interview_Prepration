
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# -----------------------------------------------------------------------------
# Concept:

# Use a dictionary to store the key to (value, frequency) mapping. Use another
# dictionary of ordereddict to store the mapping from frequency to all the keys
# with that frequency. We maintain a minimum frequency so we can get the ordereddict
# of keys with minimum frequency. Ordereddict stores insert order of keys, so by
# popping from the head of the ordereddict when reaching capacity, we remove the
# least recent used key that also has the lowest frequency.
# -----------------------------------------------------------------------------

from collections import OrderedDict
from collections import defaultdict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyToValFreq = {}  # K: key, V: (val, freq)
        # E.g. { freq 1 : {2 : None, 4 : None, 6: None}, freq 2 : {1 : None, 3 : None, 5 : None} }
        self.freqToKeyValue = defaultdict(OrderedDict)  # K: freq, V: {key : None}
        self.capacity = capacity  # self.capacity does not change
        self.minFreq = 1  # reset to 1 when new element added

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToValFreq:
            return -1
        val, freq = self.keyToValFreq.pop(
            key)  # Get the val and freq from regular dict since its present in keyToValFreq

        self.freqToKeyValue[freq].pop(key)  # Now the oldest or least frequent by popping from OrderedDict.
        self.freqToKeyValue[freq + 1][key] = None  # Update the freq dict, sice we are accessing

        self.keyToValFreq[key] = (val, freq + 1)  # Also update in this dict also for freq

        if len(self.freqToKeyValue[
                   freq]) == 0 and freq == self.minFreq:  # Conner case where we update the global minFreq variable
            self.minFreq = freq + 1

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Need to handle edge case of LFU cache capacity = 0.
        if self.capacity <= 0:
            return

        if key in self.keyToValFreq:
            self.get(key)  # Update the key freq in dict.  # NOTICE, put makes count+1 too
            self.keyToValFreq[key] = (value, self.keyToValFreq[key][1])
            return

        # Easy- If dict is getting bigger than capacity, delete item with min freq.
        if self.capacity <= len(self.keyToValFreq):
            delKey, _ = self.freqToKeyValue[self.minFreq].popitem(
                last=False)  # popitem(last=False) is FIFO, like queue it return key, val
            self.keyToValFreq.pop(delKey)

        # Regular operation of insertion to dict and updating OrderedDict too with freq.
        self.keyToValFreq[key] = (value, 1)
        self.freqToKeyValue[1][key] = None
        self.minFreq = 1

# This link is similar:
# https://leetcode.com/problems/lfu-cache/discuss/166683/Python-only-use-OrderedDict-get-O(1)-put-O(1)-Simple-and-Brief-Explained!!!!!!

################################################################################

# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation:-Two-dict-+-Doubly-linked-list
