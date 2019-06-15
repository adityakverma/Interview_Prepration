
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array
#  to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
#  by one position. Return the max sliding window.

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

#######################################################################################################

import heapq as h

class Solution(object):
    def get_next_max(self, heap, start):
        while True:
            x, idx = h.heappop(heap)
            if idx >= start:
                return x * -1, idx

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        heap = []

        for i in range(k):  # Make first Window, and then keep sliding - start + 1, end + 1
            h.heappush(heap, (nums[i] * -1, i))
        result, start, end = [], 0, k - 1

        while end < len(nums):
            x, idx = self.get_next_max(heap, start)
            result.append(x)
            h.heappush(heap, (x * -1, idx))
            start, end = start + 1, end + 1
            if end < len(nums):
                h.heappush(heap, (nums[end] * -1, end))
        return result

        # Algorithm: Max Heap Solution: O(NlogN)
        # ==========
        # Add k elements and their indices to heap. Python has min-heap. So for max-heap, multiply by -1.
        # Set start = 0 and end = k-1 as the current range.
        # Extract the max from heap which is in range i.e. >= start. Add the max to the result list. Now add the max back to the heap - it could be relevant to other ranges. That's why when we pop, we are checking index in get_next_max()
        # Move the range by 1. Add the new last number to heap.
        # This is an O(NlgN) solution.

        # CONCEPT: https://riptutorial.com/algorithm/example/25071/sliding-window-algorithm-basic-information
        # CODE: https://leetcode.com/problems/sliding-window-maximum/discuss/65957/Python-solution-with-detailed-explanation
        # Time Complexity: O(NlogN)


    '''

# Brute Force: O(n * k): BUT - Time Limit Exceeded

    def get_max(self, nums, start, end):
        answer = -2**31
        for i in range(start, end+1):
            answer = max(answer, nums[i])
        return answer
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        start,end = 0,k-1
        result = []
        while end < len(nums) and len(nums):
            result.append(self.get_max(nums, start, end))
            start, end = start+1, end+1                         # Increment the window
        return result

    # https://leetcode.com/problems/sliding-window-maximum/discuss/65957/Python-solution-with-detailed-explanation
    '''

    '''
    # My Brute force approach, which works too. passes 8/18 testcases

    def maxSlidingWindow(self, nums, k):
    
        if nums is None or k == 0:
            return []
    
        dp = [0 for _ in range(len(nums)-k+1)]
        cur_max = 0
    
        for i in range(len(nums)-k+1):
            for j in range(i, i+k):
                cur_max = max(nums[j],cur_max)
            dp[i] = cur_max 
    
        return dp

    '''


'''

Sliding window algorithm is used to perform required operation on specific window size of given large buffer or array. Window starts from the 1st element and keeps shifting right by one element. The objective is to find the minimum k numbers present in each window. This is commonly know as Sliding window problem or algorithm.
For example to find the maximum or minimum element from every n element in given array, sliding window algorithm is used.
Example:
Input Array: [1 3 -1 -3 5 3 6 7]
Window Size: 3
Maximum element from every 3 element of input array:
+---------------------------------+---------+
|      Windows Position           |   Max   |
+------------+----+---+---+---+---+---------+
|[1   3   -1]| -3 | 5 | 3 | 6 | 7 |    3    |
+------------+----+---+---+---+---+---------+
| 1 |[3   -1   -3]| 5 | 3 | 6 | 7 |    3    |
+---+-------------+---+---+---+---+---------+
| 1 | 3 |[-1   -3   5]| 3 | 6 | 7 |    5    |
+---+---+-------------+---+---+---+---------+
| 1 | 3 | -1 |[-3   5   3]| 6 | 7 |    5    |
+---+---+----+------------+---+---+---------+
| 1 | 3 | -1 | -3 |[5   3   6]| 7 |    6    |
+---+---+----+----+-----------+---+---------+
| 1 | 3 | -1 | -3 | 5 |[3   6   7]|    7    |
+---+---+----+----+---+-----------+---------+
Minimum element from every 3 element of input array:
+---------------------------------+---------+
|      Windows Position           |   Min   |
+------------+----+---+---+---+---+---------+
|[1   3   -1]| -3 | 5 | 3 | 6 | 7 |   -1    |
+------------+----+---+---+---+---+---------+
| 1 |[3   -1   -3]| 5 | 3 | 6 | 7 |   -3    |
+---+-------------+---+---+---+---+---------+
| 1 | 3 |[-1   -3   5]| 3 | 6 | 7 |   -3    |
+---+---+-------------+---+---+---+---------+
| 1 | 3 | -1 |[-3   5   3]| 6 | 7 |   -3    |
+---+---+----+------------+---+---+---------+
| 1 | 3 | -1 | -3 |[5   3   6]| 7 |    3    |
+---+---+----+----+-----------+---+---------+
| 1 | 3 | -1 | -3 | 5 |[3   6   7]|    3    |
+---+---+----+----+---+-----------+---------+
Methods to find the sum of 3 element:
Method 1:
First way is to use quick sort, when pivot is at Kth position, all elements on the right side are greater than pivot, hence, all elements on the left side automatically become K smallest elements of given array.
Method 2:
Keep an array of K elements, Fill it with first K elements of given input array. Now from K+1 element, check if the current element is less than the maximum element in the auxiliary array, if yes, add this element into array. Only problem with above solution is that we need to keep track of maximum element. Still workable. How can we keep track of maximum element in set of integer? Think heap. Think Max heap.
Method 3:
Great! In O(1) we would get the max element among K elements already chose as smallest K elements . If max in current set is greater than newly considered element, we need to remove max and introduce new element in set of K smallest element. Heapify again to maintain the heap property. Now we can easily get K minimum elements in array of N.


'''