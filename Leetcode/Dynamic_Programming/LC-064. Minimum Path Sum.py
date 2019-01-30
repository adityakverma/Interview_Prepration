
# Given a m x n grid filled with non-negative numbers, find a path from top left to
# bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# --------------------------------------------------------------------------------------


class Solution():

    # O(m*n) space
    def minPathSum(self, grid):

        if not grid:
            return

        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]

        dp[0][0] = grid[0][0]

        for i in xrange(1, r):  # For 0th Col, update row values. Basically update leftmost row.
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in xrange(1, c):  # For 0th row, update all col values. Basically update top row
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]   # Update all cells except top row and left most column.

        return dp[-1][-1]


    # change the grid itself.  DP, No extra space
    def minPathSum4(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])

        for i in xrange(1, c):
            grid[0][i] = grid[0][i] + grid[0][i-1]

        for i in xrange(1, r):
            grid[i][0] = grid[i][0] + grid[i-1][0]

        for i in xrange(1, r):
            for j in xrange(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
