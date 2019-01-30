

import heapq

# Important - heapify creates MIN Heap by default.

listForTree1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree1)             # for a min heap
print "\nMin Heap:", listForTree1


listForTree2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq._heapify_max(listForTree2)        # for a maxheap!!
print "\nMax Heap:", listForTree2
