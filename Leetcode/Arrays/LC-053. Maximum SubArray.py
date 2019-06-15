
# Tags: Array, Dynamic Programming, Divide & Conquer, Microsoft, LinkedIn
# ========================================================================

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and
# return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution():
    def maxSubArray(self, A):
        current = 0
        result = A[0]
        for i in range(len(A)):
            #print "CUR, A[i]", current, A[i]
            current += A[i]
            result = max(current,result)
            #print "Current result ", (current, result)
            current = max(0,current)
            #print current
        return result

    def maxSubArray2(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1]+ nums[i], nums[i])
        return max(nums)

    def maxSubArray_DP(self, nums): # OKKK ....
        if not nums:
            return None
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            #res = max(res, dp[i])
            #print dp
        return max(dp)

    # DP, O(n) space
    def maxSubArray4(self, nums):
        if not nums:
            return None
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [-2,-3,6,-8,2,-9]

    s = Solution()
    #print s.maxSubArray(nums)
    #print s.maxSubArray2(nums)
    print s.maxSubArray_DP(nums)

    print s.maxSubArray4(nums)

# I was asked a follow up question to this question in an interview." How would we solve this given that there is an endless incoming stream of numbers ?" Ideas anybody?
# https://leetcode.com/problems/maximum-subarray/discuss/179894/Follow-up-question-in-Intervierw


#  maxSubArray(): Python Greedy Solution:
#  The idea is that as long as you are above 0, you've retained the
#  "biggest number" somewhere along the line.
#  once you go below 0 the chain can no longer be the best chain so reset it.
#  Should be pretty easy to follow. O(n)
#  complexity, so obviously not the most optimal, but 76ms.

# https://leetcode.com/problems/maximum-subarray/discuss/20537/Python-Greedy-Solution
# https://leetcode.com/problems/maximum-subarray/discuss/20487/Python-solutions-(DP-O(n)-space-O(1)-space).
