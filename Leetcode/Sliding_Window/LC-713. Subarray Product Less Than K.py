

# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
#
# Example 1:
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# ========================================================================================

class Solution(object):

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        prod = 1
        ans = left = 0

        for right, val in enumerate(nums):
            prod *= val

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right - left + 1
        return ans

# Concept: SLIDING WINDOW:
# Two pointer O(n) time O(1) space:
# Initialize a left index j = 0 and a right index i = 0. As we iterate i over range(len(nums)),
# we keep updating res, the cumulative product of all entries from j to i. As soon as res >= k,
# we move the left index to the right until res < k. The length i - j + 1 is then the number of subarrays
# ending with i where the product of all elements in the subarray is less than k.

# In other words:
# # Our loop invariant is that left is the smallest value so that the product in the window prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.
# For every right, we update left and prod to maintain this invariant. Then, the number of intervals with subarray product less than k and with right-most coordinate right, is right - left + 1. We'll count all of these for each value of right.

