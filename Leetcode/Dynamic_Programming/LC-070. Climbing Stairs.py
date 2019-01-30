
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# --------------------------------------------------------------------------

class Solution():

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)  # the way to declare the array. Note its different from list.

        if n == 0: return 1
        if n == 1: return 1
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # If n =5, so No on of ways to reach 4 plus 1 step ( dp[4] +1) plus no of ways to reach 3 plus 2 (dp[3] +2)

        return dp[n]
