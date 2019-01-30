
# https://docs.python.org/3.6/library/heapq.html

# This module provides an implementation of the heap queue algorithm, also known as
# the priority queue algorithm.
#
# Heaps are binary trees for which every parent node has a value less than or equal to
# any of its children. This implementation uses arrays for which heap[k] <= heap[2*k+1]
# and heap[k] <= heap[2*k+2] for all k, counting elements from zero.

# READ THAT LINK .... PLZZZZ



##################  NOTE - TREE-MAP #################
# https://www.interviewbit.com/courses/programming/topics/heaps-and-maps/

# Python does not have a implementation of treemap in standard library
# The closes we come to it is with heapq which is implementation of heaps
# ( http://en.wikipedia.org/wiki/Heap_%28data_structure%29 ) which obviously
# means that we are restricted in terms of number of things we can do as
# compared to treemap.
#
# Heap declaration :
#
#     A = []; # declares an empty list / heap. O(1)
#             # Note that heaps are internally implemented using lists for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k.
#
# Insert a new key, value pair K, V:
#
#     heapq.heappush(A, (K, V));     // O(log n)
#
# Delete the smallest key K ( Note that deleting random key K will be inefficient ) :
#
#     heapq.heappop(A)[0]
#
# Find minimum key K in the map ( if the map is not empty ) :
#
#     A[0][0]
#
# Size ( number of entries in the map ) :
#
#     len(A)

