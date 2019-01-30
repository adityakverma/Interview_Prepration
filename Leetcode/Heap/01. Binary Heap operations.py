# A Python program to demonstrate common binary heap operations
# https://www.geeksforgeeks.org/binary-heap/

# ---------------------------------------------------------------------------
# [Aditya] : Introduction: Heaps are binary trees for which every parent
# node has a value less than or equal to any of its children.
# Operation of heapq DS are:

# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap invarient
# heapify - transform list into heap, in place, in linear time

# Operation in MinHeap : https://www.youtube.com/watch?v=uZj0hetLFHU
# --------------------
# Note extractMin() is removing min from root, which is opposite of insert().
# But delete(i) is deleting any specific key from anywhere in tree unlike
# extractMin.
#
# So in delete(i, -infi), we first replace that key with -ve infinite and
# do minHeapify ( by calling decereaseKey()). So root has now -infi. Now we
# do extractMin(), which will delete root (-infi) and move last element of heap
# to root and again re-adjust nodes (minHeapify)  as per for minHeap property.
#
# getMin() is just getting root value heap[0] ( not extracting or
# removing). Basically we re-adjust( minHeapify) twice when we delete node 'i'

# Applications of Heap :
# ----------------------
# Priority Queue are implemented using Binary Heap because it supports
# insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time
# In other words, Heap DS (Binary heap or MinHeap) is used to represent
# Priority Queue.

# Priority Queue is similar to queue where we insert an element from the back and
# remove an element from front (FIFO or LILO) , but with a difference that the logical
# order of elements in the priority queue depends on the priority of the elements. The
# element with highest priority will be moved to the front of the queue and one with
# lowest priority will move to the back of the queue. Thus it is possible that when
# you enqueue an element at the back in the queue, it can move to front because of its
# highest priority.
# ----------------------------------------------------------------------------

# Import the heap functions from python library
from heapq import heappush, heappop, heapify

# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):

        self.heap[i] = new_val

        # Now heapify. Note for insert and delete key -MinHeapify is taken
        # care by heappush and heappop inbuild functions itself.
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])

    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin() and then minheapify()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

if __name__ == '__main__':

    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    print "\nOriginal Heap: ",heapObj.heap

    heapObj.deleteKey(1)  # This functon deletes key at index i.
    print "\nHeap after deleting at index 1: ",heapObj.heap

    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)
    print "\nHeap after inserting 15,5,4,45: ", heapObj.heap

    print "\nExtract Min: ",heapObj.extractMin()
    print "Heap after extractMin: ",heapObj.heap

    print "\nGet Min: ",heapObj.getMin()

    heapObj.decreaseKey(2, 1)
    print "\nHeap after decreaseKey(2,1): ",heapObj.heap
    print "Get Min: ", heapObj.getMin()

###################################################################################

