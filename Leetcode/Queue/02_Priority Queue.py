
# https://www.geeksforgeeks.org/priority-queue-set-1-introduction/

# #
# Priority Queue | Set 1 (Introduction)
#
# Priority Queue is an extension of queue with following properties.
# 1) Every item has a priority associated with it.
# 2) An element with high priority is dequeued before an element with low priority.
# 3) If two elements have the same priority, they are served according to their order in the queue.
#
# A typical priority queue supports following operations.
# insert(item, priority): Inserts an item with given priority.
# getHighestPriority(): Returns the highest priority item.
# deleteHighestPriority(): Removes the highest priority item.
#
# How to implement priority queue?
# Using Array: A simple implementation is to use array of following structure.
#
# struct item {
#    int item;
#    int priority;
# }
#
# insert() operation can be implemented by adding an item at end of array in O(1) time.
#
# getHighestPriority() operation can be implemented by linearly searching the highest priority item in array. This operation takes O(n) time.
#
# deleteHighestPriority() operation can be implemented by first linearly searching an item, then removing the item by moving all subsequent items one position back.
#
# We can also use Linked List, time complexity of all operations with linked list remains same as array.
# The advantage with linked list is deleteHighestPriority() can be more efficient as we dont have to move items.
#
# Using Heaps:
# Heap is generally preferred for priority queue implementation because heaps provide better performance compared arrays or linked list. In a Binary Heap, getHighestPriority() can be implemented in O(1) time, insert() can be implemented in O(Logn) time and deleteHighestPriority() can also be implemented in O(Logn) time.
# With Fibonacci heap, insert() and getHighestPriority() can be implemented in O(1) amortized time and deleteHighestPriority() can be implemented in O(Logn) amortized time.
#
# Applications of Priority Queue:
# 1) CPU Scheduling
# 2) Graph algorithms like Dijkstras shortest path algorithm, Prims Minimum Spanning Tree, etc
# 3) All queue applications where priority is involved.


# A priority queue is typically implemented using Heap data structure.
#
# Applications:
#
# Dijkstra’s Shortest Path Algorithm using priority queue: When the graph is stored in the form of adjacency list or matrix, priority queue can be used to extract minimum efficiently when implementing Dijkstra’s algorithm.
#
# Prim’s algorithm: It is used to implement Prim’s Algorithm to store keys of nodes and extract minimum key node at every step.

# https://docs.python.org/3.6/library/heapq.html

