
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different. You have to paint
# all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost
# matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2]
# is the cost of painting house 1 with color 2, and so on... Find the minimum cost to
#  paint all houses.

#
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, 1 with green, 2 with blue
# Min Cost = 2+5+3 = 10

# Note: Since we choose blue(cost=2) for house as its min, so we cannot choose same color
# for adjacent house, hence we choose either red(cost=16) or green(cost=5) for house 2 and so on..
#
# ------------------------------------------------------------------------------------

class Solution(object):  # LinkedIn
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 :  # Since we have no house to paint
            return 0

        for i in range(1,len(costs)):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])  # Cumulative add - min of other two previous values to get min at current position
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][0],costs[i-1][1])

        return min( min(costs[-1][0],costs[-1][1]), costs[-1][2]) # Basically min of last row, since that will have cumulative minimum

# https://www.youtube.com/watch?v=fZIsEPhSBgM
# ---------------------------------------------------------------------------
# DP

class Solution_(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        dp = [[0 for i in range(3)] for j in range(len(costs))]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        i = 1
        while i < len(costs):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
            i += 1

        return min(dp[i-1][0], min(dp[i-1][1], dp[i-1][2]))

