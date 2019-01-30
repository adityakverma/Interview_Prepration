
# Tags: Array, DP, Amazon

#  On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum
# cost to reach the top of the floor, and you can either start from the step with index 0,
# or the step with index 1.
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# =================================================================================

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost))

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])

        return min(dp[-2], dp[-1])  # OR simply return dp[-1]

    # Good Link to see soltion both TopDown and BottomUp methods:
    # https://leetcode.com/problems/min-cost-climbing-stairs/discuss/212517/python

# ==================================================================================

## Recursive solution
class Solution1:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        lib = {}
        cost = cost + [0]
        return self.climb(cost, len(cost) - 1, lib)

    def climb(self, cost, n, lib):
        if n == 0:
            return cost[0]
        elif n == 1:
            return cost[1]
        else:
            if n in lib:
                return lib[n]
            tmp = min(self.climb(cost, n - 2, lib), self.climb(cost, n - 1, lib)) + cost[n]
            lib[n] = tmp
            return tmp


## Iterative solution
class Solution2:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)

        for idx in range(len(cost)):
            if idx < 2:
                dp[idx] = cost[idx]
            else:
                dp[idx] = min(dp[idx - 2], dp[idx - 1]) + cost[idx]
        return dp[len(cost) - 1]