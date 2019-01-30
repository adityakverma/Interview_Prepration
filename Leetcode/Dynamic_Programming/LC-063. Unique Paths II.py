
# A robot is located at the top-left corner of a m x n grid
#  (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in
# time. The robot is trying to reach the bottom-right corner of
# the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How
# many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# =========================================================================================

# https://leetcode.com/problems/unique-paths-ii/discuss/146073/Python-DP-beat-100-python-submissions
# https://leetcode.com/problems/unique-paths-ii/discuss/23256/Accepted-python-solutionbeats-99.79

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for x in range(M)] for y in range(N)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0 # Because we cannot start since starting point itself is obstacle.

        for i in range(N):
            for j in range(M):

                if obstacleGrid[i][j] == 1:  # If we find obstacle
                    dp[i][j] = 0  # Mark that cell as 0 in dp matrix. and it reduces path count for next futher cells meaning that path was eleminated and count decreses.
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1] # Basically for first row, if any col is blocked then successive columns in that first row also get blacked
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j] # Similarly for first col, if above row was blocking, then all below are blocked too.
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]

    # Note in these problems first row and first col are special.
    # First row gets all values from its immediate left cell.
    # First Col gets all values from its immediate upper cell.


