
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

# Similar Problem: [85. Maximal Rectangle]
# -------------------------------------------------------------------------

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(0, n)] for i in range(0, m)]  # Just copy matrix to dp array.

        for i in range(1, m):  # Note: We consider from 2nd row & col onwards, so we can check previous row and cols for min square.
            for j in range(1, n):

                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # Check
                else:
                    dp[i][j] = 0

        res = max(max(row) for row in dp)
        return res ** 2

    # Check this video to Tushar Roy : https://www.youtube.com/watch?v=_Lf1looyJMU
    # O(mn) time and O(mn) space

