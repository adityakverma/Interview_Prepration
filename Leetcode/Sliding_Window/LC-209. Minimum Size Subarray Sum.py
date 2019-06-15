
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
# subarray of which the sum ≥ s. If there is not one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
# ================================================================================================================


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Using Sliding Window Algorithm: - See below explanation

        minLen = len(nums) + 1
        total, start = 0, 0

        for i in range(len(nums)):
            total += nums[i]  # Get possible candidate

            # If total is not >= target, then quit while loop and add more to total (expand the window).
            # else refine candiate by moving left end to left since we need to get minimum number.
            while total >= s:
                minLen = min(minLen, i - start + 1)
                total = total - nums[start]
                start = start + 1  # Moving the window's left end now, because we need to get minmum number ele whole sum>=target

        return 0 if minLen > len(nums) else minLen


'''  
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtyp
              
        # Using Binary Search

        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.find_left(left, right, nums, s, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, s, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid
        return left

'''

'''
Sliding Window Algorithm:
========================

Trick here is to keep adding numbers from the start of array until you hit the target. 

After that we keep adding numbers from the end and subtracting numbers from the start as long as the total is still above target and keep checking if the new array is the minimum length. 

The intuition is that for example, a 10 added on the end could replace two 5's from start of array and thus the reduce the number of elements needed to hit target in that subarray.

IMP NOTE: To find maximum substring, we should update maximum after the inner while loop to guarantee that the substring is valid. On the other hand, when asked to find minimum substring, we should update minimum inside the inner while loop.

# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/211775/Python-O(N)-greater-minimum-window-substring-template
# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution

'''