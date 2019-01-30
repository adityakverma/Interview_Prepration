
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
# on it represented by array nums. You are asked to burst all the balloons. If the
# you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
# left and right are adjacent indices of i. After the burst, the left and right then
# becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#     You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
#     0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# -----------------------------------------------------------------------------

# Analysis:
# We need to find a way to divide the problems. If we start from the first balloon, we can't determine the left/right for the number in each sub-problem, If we start from the last balloon, we can.
# We can see the transformation equation is very similar to the one for matrix multiplication.
#
# dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j
#
# This is a typical interval DP problem. Because the order of the number extracted matters, we need to do a O(n^3) DP. If we only need to expand the interval to the left or right, we only need to do a O(n^2) DP.

# ------------------
#Top - down:

class Solution(object):

    # First, we define the f[i][j] (i+1<j) as the maxmium value of range we can get from range [i, j]. For example, if list is [2,2,2], f[1][3] 's maxmium value and only value is 8.
    # and the formula to calculate particular value from subset is like below. And, we could notice that, the range of subset is contained in side range (i, j), we could compute from smallest range to largest range.
    # f[i][j] = max( f[i][mid] + f[mid][j] + nums[i] * nums[mid] * nums[j] )    # i < mid < j

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        def calculate(i, j):

            if dp[i][j] or j == i + 1:  # in memory or gap < 2 ( because we added one extra ballon on each side)
                return dp[i][j]

            coins = 0
            for k in xrange(i + 1, j):  # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)

    # -------------------------------------------------------------


# This is a DP problem.
# and with O(N^3) for loop, we could get answer

#Bottom - up:

class Solution_(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        for gap in xrange(2, n):
            for i in xrange(n - gap):
                j = i + gap
                for k in xrange(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]


# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

# https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
