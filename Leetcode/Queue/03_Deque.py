
#
# Deque | Set 1 (Introduction and Applications)
#
# Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.
#
# Operations on Deque:
# Mainly the following four basic operations are performed on queue:
#
# insertFront(): Adds an item at the front of Deque.
# insertLast(): Adds an item at the rear of Deque.
# deleteFront(): Deletes an item from front of Deque.
# deleteLast(): Deletes an item from rear of Deque.
#
# In addition to above operations, following operations are also supported
# getFront(): Gets the front item from queue.
# getRear(): Gets the last item from queue.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.
#
# Applications of Deque:
# Since Deque supports both stack and queue operations, it can be used as both. The Deque data structure supports clockwise and anticlockwise rotations in O(1) time which can be useful in certain applications.
# Also, the problems where elements need to be removed and or added both ends can be efficiently solved using Deque. For example see Maximum of all subarrays of size k problem., 0-1 BFS and Find the first circular tour that visits all petrol pumps.
#

# https://www.geeksforgeeks.org/deque-in-python/
# ----------------------------------------------

# # Deque can be implemented in python using the module collections.
# Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
# as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
#
# Operations on deque :
#
# 1. append() :- This function is used to insert the value in its argument to the right end of deque.
# 2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
# 3. pop() :- This function is used to delete an argument from the right end of deque.
# 4. popleft() :- This function is used to delete an argument from the left end of deque.



# Python code to demonstrate working of
# append(), appendleft(), pop(), and popleft()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print ("The deque after appending at right is : ")
print (de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print ("The deque after appending at left is : ")
print (de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print ("The deque after deleting from right is : ")
print (de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print ("The deque after deleting from left is : ")
print (de)
