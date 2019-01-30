
# Similar to LC-215. But this is STREAM and not fixed array

# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);

# kthLargest.add(3);   // returns 4 - return element representing the kth largest element in the stream.
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8

import heapq

class KthLargest:

    # constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream.
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums) # Get MinHeap
        for _ in range(0,len(nums)-k): # After popping K elements from minHeap. Head or top of Heap will have Kth largest element at num[0]
            heapq.heappop(self.nums)     # So head or root will have kth largest

    # For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
    def add(self, val):

        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)  # you add new integer from stream to heap and then you pop so head to tree always maintains k largest number - which we can return via nums[0]
        #print "Length",len(nums)
        return self.nums[0]

if __name__ == '__main__':

    k = 3
    nums = [4,5,8,2]

    kthLargest = KthLargest(k,nums)

    print kthLargest.add(3)   # returns 4
    print kthLargest.add(5)   # returns 5
    print kthLargest.add(10)  # returns 5
    print kthLargest.add(9)   # returns 8
    print kthLargest.add(4)   # returns 8

