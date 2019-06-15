
# Tags: Array, Two Pointer, Binary Search, Facebook

# Given an array of n positive integers and a positive integer s, find the minimal length of a
# contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

import math

class Solution():

    # My Solution, but doesn't passes all TC on LC. Only few
    def minSizeSubarraySum2(self, nums, k):
        min_count = []
        count, sum = 0, 0

        if len(nums) <= 0: return 0

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum += nums[j]
                count += 1
                if sum >= k:                # contiguous subarray of which the sum >= s
                    min_count.append(count)
            sum, count = 0, 0

        if len(min_count) < 0: return 0
        return min(min_count)

    # https://leetcode.com/problems/minimum-size-subarray-sum/discuss/111449/Clean-Python-Codes:-Two-Pointers-O(n)
    # Time Complexity: O(n)
    def minSubArrayLen(self, nums,s):
        if not nums or len(nums) == 0: return 0

        i = j = 0
        total = nums[0]
        solution = 100
        while j < len(nums):
            if total < s:
                j += 1
                if j < len(nums): total += nums[j]
                #print "if", total, j
            else:
                solution = min(solution, j - i +1)
                total -= nums[i]
                i += 1
                #print "else", total, i, solution
        return 0 if solution == 100 else solution

if __name__ == '__main__':

    nums1 = [2, 3, 1, 2, 4, 3]
    nums = [1,2,3,4,5]
    k1 = 7
    k = 11
    s = Solution()
    print "\nMin Size of Subarray with sum %d is %d" %(k,s.minSizeSubarraySum2(nums1,k1))

    print "\nMin Size of Subarray with sum %d is %d" %(k,s.minSubArrayLen(nums1,k1))



#     What is the difference between 'Time Limit Exceeded' and 'Timeout'?
#
#     If your solution is judged 'Time Limit Exceeded', it could be:
#
#     Your code has an underlying infinite loop.
#     Your algorithm is too slow and has a high time complexity.
#     The data structure you returned is in an invalid state. For example, a linked list that contains a cycle.