
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# ----------------------------------------------------------------------------------

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp_max = [0] * n  # DP array to maintain max
        dp_min = [0] * n  # DP array to maintain min - Becoz in case like [2,3,-2,-4] we have two -ve so this array will help to get +48
        dp_max[0], dp_min[0] = nums[0], nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])

            elif nums[i] < 0:
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])

            else:
                dp_max[i] = 0
                dp_min[i] = 0

        # print (dp_max, dp_min)
        return max(dp_max)

