
# https://docs.python.org/3.6/library/collections.html#deque-objects

# Deques are a generalization of stacks and queues. Deques support thread-safe,
# memory efficient appends and pops from either side of the deque with approximately
# the same O(1) performance in either direction.

# Though list objects support similar operations, they are optimized for fast
# fixed-length operations and incur O(n) memory movement costs for pop(0) and
# insert(0, v) operations which change both the size and position of the underlying
# data representation.
#

# deque provides you with a double ended queue which means that you can append and
# delete elements from either side of the queue. First of all you have to import the
# deque module from the collections library:


from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())


d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print d                                # show the representation of the deque
#deque(['f', 'g', 'h', 'i', 'j'])

d.pop()                          # return and remove the rightmost item
#'j'
d.popleft()                      # return and remove the leftmost item
#'f'
list(d)                          # list the contents of the deque
#['g', 'h', 'i']
print d[0]                             # peek at leftmost item
#'g'
print d[-1]                            # peek at rightmost item
#'i'

list(reversed(d))                # list the contents of a deque in reverse
#['i', 'h', 'g']
print 'h' in d                         # search the deque
#True

d.extend('jkl')                  # add multiple elements at once
print d
#deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.rotate(1)                      # right rotation
print d
#deque(['l', 'g', 'h', 'i', 'j', 'k'])

d. rotate(-1)                     # left rotation
print d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

print deque(reversed(d))               # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])
# >>> d.clear()                        # empty the deque
# >>> d.pop()                          # cannot pop from an empty deque
# Traceback (most recent call last):
#     File "<pyshell#6>", line 1, in -toplevel-
#         d.pop()
# IndexError: pop from an empty deque
#
# >>> d.extendleft('abc')              # extendleft() reverses the input order
# >>> d
# deque(['c', 'b', 'a'])

# --------------------------------------------------------------------------
# Bounded length deques provide functionality similar to the tail
# filter in Unix:
#
# def tail(filename, n=10):
#     'Return the last n lines of a file'
#     with open(filename) as f:
#         return deque(f, n)
# --------------------------------------------------------------------------
# The rotate() method provides a way to implement deque slicing and deletion.
# For example, a pure Python implementation of del d[n] relies on the rotate()
# method to position elements to be popped:
#
# def delete_nth(d, n):
#     d.rotate(-n)
#     d.popleft()
#     d.rotate(n)

####################################################################################

# https://www.geeksforgeeks.org/deque-in-python/

# #
# Deque in Python
#
# Deque can be implemented in python using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
#
# Operations on deque :
#
# 1. append() :- This function is used to insert the value in its argument to the right end of deque.
#
# 2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
#
# 3. pop() :- This function is used to delete an argument from the right end of deque.
#
#
# 4. popleft() :- This function is used to delete an argument from the left end of deque.
# filter_none
#
# edit
#
# play_arrow
#
# brightness_4
# # Python code to demonstrate working of
# # append(), appendleft(), pop(), and popleft()
#
# # importing "collections" for deque operations
# import collections
#
# # initializing deque
# de = collections.deque([1,2,3])
#
# # using append() to insert element at right end
# # inserts 4 at the end of deque
# de.append(4)
#
# # printing modified deque
# print ("The deque after appending at right is : ")
# print (de)
#
# # using appendleft() to insert element at right end
# # inserts 6 at the beginning of deque
# de.appendleft(6)
#
# # printing modified deque
# print ("The deque after appending at left is : ")
# print (de)
#
# # using pop() to delete element from right end
# # deletes 4 from the right end of deque
# de.pop()
#
# # printing modified deque
# print ("The deque after deleting from right is : ")
# print (de)
#
# # using popleft() to delete element from left end
# # deletes 6 from the left end of deque
# de.popleft()
#
# # printing modified deque
# print ("The deque after deleting from left is : ")
# print (de)
#
# Output:
#
# The deque after appending at right is :
# deque([1, 2, 3, 4])
# The deque after appending at left is :
# deque([6, 1, 2, 3, 4])
# The deque after deleting from right is :
# deque([6, 1, 2, 3])
# The deque after deleting from left is :
# deque([1, 2, 3])
#
# 5. index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
#
# 6. insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
#
# 7. remove() :- This function removes the first occurrence of value mentioned in arguments.
#
# 8. count() :- This function counts the number of occurrences of value mentioned in arguments.
# filter_none
#
# edit
#
# play_arrow
#
# brightness_4
# # Python code to demonstrate working of
# # insert(), index(), remove(), count()
#
# # importing "collections" for deque operations
# import collections
#
# # initializing deque
# de = collections.deque([1, 2, 3, 3, 4, 2, 4])
#
# # using index() to print the first occurrence of 4
# print ("The number 4 first occurs at a position : ")
# print (de.index(4,2,5))
#
# # using insert() to insert the value 3 at 5th position
# de.insert(4,3)
#
# # printing modified deque
# print ("The deque after inserting 3 at 5th position is : ")
# print (de)
#
# # using count() to count the occurrences of 3
# print ("The count of 3 in deque is : ")
# print (de.count(3))
#
# # using remove() to remove the first occurrence of 3
# de.remove(3)
#
# # printing modified deque
# print ("The deque after deleting first occurrence of 3 is : ")
# print (de)
#
# Output:
#
# The number 4 first occurs at a position :
# 4
# The deque after inserting 3 at 5th position is :
# deque([1, 2, 3, 3, 3, 4, 2, 4])
# The count of 3 in deque is :
# 3
# The deque after deleting first occurrence of 3 is :
# deque([1, 2, 3, 3, 4, 2, 4])
#
# 9. extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
#
# 10. extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.
#
# 11. reverse() :- This function is used to reverse order of deque elements.
#
# 12. rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.
