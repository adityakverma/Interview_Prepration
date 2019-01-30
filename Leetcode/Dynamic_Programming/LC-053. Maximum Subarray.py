# Tags: Array, Dynamic Programming, Divide & Conquer, Microsoft, LinkedIn
# ========================================================================
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and
# return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6;  Explanation: [4,-1,2,1] has the largest sum = 6.

# ALSO check LC 152 - Same concept
class Solution():

    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1]+ nums[i], nums[i])
        return max(nums)

    # Using Dynamic Programming. O(n) Space : Looks like Kadane
    def maxSubArray_DP(self, nums): # OKKK ....
        if not nums:
            return None

        dp = [0] * len(nums)
        res = dp[0] = nums[0]

        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i]) # we need to find that contiguous portion of an array where the sum is maximum.
            #res = max(res, dp[i])
            #print dp
        return max(dp)

    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     if not prices:
    #         return 0
    #
    #     curSum = maxSum = 0
    #     for i in range(1, len(prices)):
    #         curSum = max(0, curSum + prices[i] - prices[i - 1])
    #         maxSum = max(maxSum, curSum)
    #
    #     return maxSum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [-2,-3,6,-8,2,-9]

    s = Solution()
    #print s.maxSubArray(nums)
    print s.maxSubArray_DP(nums)
    #print s.maxProfit(nums)

# I was asked a follow up question to this question in an interview." How would we solve this given that there is an endless incoming stream of numbers ?" Ideas anybody?
# https://leetcode.com/problems/maximum-subarray/discuss/179894/Follow-up-question-in-Intervierw
