
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Return
# the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# https://leetcode.com/problems/sliding-window-maximum/discuss/65957/Python-solution-with-detailed-explanation
# https://leetcode.com/problems/sliding-window-maximum/discuss/65957/Python-solution-with-detailed-explanation

from heapq import heappush, heappop, heapify
import collections

class Solution(object):

    '''
    #----------------------------------------------------------------------------
    def maxSlidingWindow_(self, nums, k):
        if len(nums) == 0:
            return 0
        if len(nums) < k:
            return nums

        res = []
        pq =  [] # Priority Queue - MaxHeap

        for i in range(len(nums)):
            if i < k:
                heappush(pq, -nums[i])
                print pq
            else:
                #
                res.append(-pq[0])
                print "Result",nums[i]
                #heappop(pq)
                heappush(pq, -nums[i])
                print "...............Heap",(pq)

        return

#  Note: In above you want to remove i-kth element when shifting window, but
#  for that heappop will not help, because heappop will remove min element from
# root. If you had Priority Queue implemented then
#  you would have deleted [n-k] element easily. Just like we implemented
#  deleteKey() in Binary Heap or PQ.


    def maxSlidingWindow(self, nums, k):
        cnt, heap, res = collections.Counter(), [], []
        for i, num in enumerate(nums):

            heappush(heap, -num) # Create MaxHeap

            cnt[num] += 1 # Increment counter for that number. Adding entry for that num

            print "count",cnt[num]
            print cnt.items()
            print "Top" , cnt[-heap[0]]

            print ".........Heap    ", heap

            while not cnt[-heap[0]]:
            #    print "..",cnt[-heap[0]]
                heappop(heap)
                print "##########################"
            print ".........Heap pop", heap
            if i >= k - 1:
                res.append(-heap[0])  # Appending to Result
                cnt[nums[i - k + 1]] -= 1 # Remove that first element in window so there is space to add next element. aka move window.
        return res

'''


    def maxSlidingWindow_B1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        sol = []
        for i in range(0, len(nums) - k + 1):
            sol.append(max(nums[i:i + k]))

        return sol

    def maxSlidingWindow_B2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        sol = []
        queue = []
        for i in range(0, len(nums)):

            while queue and nums[queue[-1]] < nums[i]: # update the queue
            # pop from right end as values (which is nums[queue[-1]] here) less than nums[i] are of no use
                #print "Queue before pop (indexes): ",queue
                queue.pop()

            queue.append(i) # Note we are appending index.

            if queue[0] == i - k: # # judge whether the first item is in window
                queue.pop(0)

            if i >= k - 1:
                sol.append(nums[queue[0]])

        return sol

if __name__ == '__main__':
    s = Solution()

    nums = [1, 3, 10, -1, -3, 5, 3, 6, 7, -6]
    k = 3

    print s.maxSlidingWindow_B1(nums, k)
    print s.maxSlidingWindow_B2(nums, k)


'''

# https://leetcode.com/problems/sliding-window-maximum/discuss/66034/Python-Solution-with-deque

 class Solution(object):
        def maxSlidingWindow(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            queue = [] # like PriorityQueue, remain the top k value
            result = []
    
            for i in xrange(len(nums)):
                # judge whether the first item is in window
                if queue and queue[0] < i - k + 1:
                    queue.pop(0)
    
                # update the queue 
                while queue and nums[queue[-1]] < nums[i]:
                    queue.pop()
    
                queue.append(i)
                
                #after i > k - 1, output the max value
                if queue and i >= k - 1:
                    result.append(nums[queue[0]])
        return result
        
'''


