
# Find the kth largest element in an unsorted array. Note that it is the kth largest
# element in the sorted order, not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

##################################################################

# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60535/Python-min-heap-and-quick-partition-solutions-(O(nlogn)-and-O(n)-time-complexities).
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/140217/Clear-Python-Solutions:-headq-sort-quickselect-(recursive-and-iterative)
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).

# Time Complexity - min-heap solutions takes O(k+(n-k)lgk) time
# Space Complexity = O(k).. If you want to improve space complexity then use Quick sort where we do in-place. so it becomes O(1)

import heapq

class Solution():

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
        heap = nums[:]
        heapq.heapify(heap) # create a min-heap whose size is k. This takes nlogk. log k is to minHeapify for adding n element to heap

        for _ in range(len(heap)-k): # Because its min heap so everytime you pop you get min element. so to get kth largest you need to pop len(heap)-k elements before we actually get Kth largest.
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # Similar Solution
    def findKthLargest2(self, nums, k): # Mine

        heapq.heapify(nums)  # So num is minHeap

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]

    def findKthLargest(self, nums, k):
        res =0
        heap=[]

        for i in nums:
            heapq.heappush(heap,-i)  # Nice Trick - make all negative using min heap. Also another way to create heap instead us using heapify

        for i in range(k):
            res = -heapq.heappop(heap)
        return res

    ##########################################################################

    # Quick Sort - O(n) - Partition method
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def findKthLargest_quickSort(self, nums, k):
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest_quickSort(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest_quickSort(nums[pos+1:], k)
        else:
            return nums[pos]


# Aditya: heapify creates MinHeap ( NOT MaxHeap )

if __name__ == '__main__':

    s = Solution()
    Input = [3, 2, 1, 5, 6, 4]
    k = 2
    print "\nKth largest (Using Heap):",s.findKthLargest(Input,k)
    print "\nUsing Quick Sort:",s.findKthLargest_quickSort(Input,k)


#----------------------------------------------------------

'''
import heapq
listForTree1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree1)             # for a min heap
print "\nMin Heap:", listForTree1

listForTree2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq._heapify_max(listForTree2)        # for a maxheap!!
print "\nMax Heap:", listForTree2

'''


# Kth Largest Element in a Stream

'''

# LC-703 

class KthLargest:

    # constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream.
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums) # Get MinHeap
        while len(self.nums) > k:
            heapq.heappop(self.nums)  # After popping K elements from minHeap. Head or top of Heap will have Kth largest element at num[0]


    # For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
    def add(self, val):

        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)  # you add new integer from stream to heap and you pop, so head to tree maintains or will have Kth largest number - which we can return via nums[0]
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
    
'''