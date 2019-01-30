
# A robot is located at the top-left corner of a m x n grid (marked
#  'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
# Above  image is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:

# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# --------------------------------------------------------------------------------

# https://leetcode.com/problems/unique-paths/discuss/23204/44ms-Python-DP-solution
# https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).


# Concept:
# Note in these problems first row and first col are special.
# First row gets all values as 1, as no. of ways to reach any col of first row is 1 way which is horizonatlly.
# First Col gets all values as 1, as no. of ways to reach any row of first col is 1 way only.
# Remaining cells get updated based on formula dp[i][j] = dp[i][j - 1] + dp[i - 1][j] because its sum of up and left cell.

class Solution:
    def uniquePaths(self, m, n):

        dp = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]  # Update all cells except top row and left most column.
        return dp[-1][-1]

        # Note-1: aux[-1][-1]  is just accessing the bottom right cell in the grid which contains the unique number of paths to get to that cell, which is the answer

        # Could you please explain why the aux matrix is initialized with all 1s? Thank you!
        # I don't think they all have to be ones, but the first column and first row must be 1's since there is only one path to get there (i.e. to get anywhere in the first row you must have just done all right moves and similarly for the first column you must have just done all down moves). With that initialized you can just use the update rule to fill in the rest of the cells (those 1's would be overwritten)

# -----------------------------------------------------------------------------------

# https://leetcode.com/problems/unique-paths/discuss/23239/One-line-in-Python
# https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space?page=2

# It's true that this can be solved with dynamic programming. But you can see that
# every path has exactly m - 1 horizontal moves and n - 1 vertical moves. So, to
# get a particular path, you need to choose where to put your m - 1 horizontal
# moves (or your n - 1 vertical moves) amongst the m + n - 2 total moves.
# That gives (m+n-2 choose m-1) paths (or (m+n-2 choose n-1), which is the same).

import math
class Solution_:
    # @return an integer
    def uniquePaths(self, m, n):
        return math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))

