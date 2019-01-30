
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

# The property of this data structure in python is that each
# time the smallest of heap element is popped(min heap).

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)
print "Original HEAP", li


# printing created heap
print "\nThe created heap is : ",
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li ,4)

# printing modified heap
print "\nThe modified heap after push 4 is : ",
print (list(li))

# using heappop() to pop smallest element
print "\nThe popped and smallest element is : ",
print (heapq.heappop(li))
print "Current HEAP", li


###################################################################

# 4. heappushpop(heap, ele) :- This function combines the functioning of
# both push and pop operations in one statement, increasing efficiency.
# Heap order is maintained after this operation.

# 5. heapreplace(heap, ele) :- This function also inserts and pops element
# in one statement, but it is different from above function. In this,
# element is first popped, then element is pushed.i.e, the value larger
# than the pushed value can be returned.

print "\n------------------------------------------------"

# Python code to demonstrate working of
# heappushpop() and heapreplce()

# importing "heapq" to implement heap queue
import heapq

# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print "\nThe popped item using heappushpop() is : ",
print (heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously pops 3
# element is first popped- which is 3, then element is pushed.

print "\nThe popped item using heapreplace() is : ",
print (heapq.heapreplace(li2, 2))

##################################################################

# 6. nlargest(k, iterable, key = fun) :- This function is used to return the k
# largest elements from the iterable specified and satisfying the key if
# mentioned.

# 7. nsmallest(k, iterable, key = fun) :- This function is used to return the
#  k smallest elements from the iterable specified and satisfying the key if
# mentioned.

# Python code to demonstrate working of
# nlargest() and nsmallest()

print "\n------------------------------------------------"

# importing "heapq" to implement heap queue
import heapq

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print "\nThe 3 largest numbers in list are : ",
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print "\nThe 3 smallest numbers in list are : ",
print(heapq.nsmallest(3, li1))

print "\n------------------------------------------------"
