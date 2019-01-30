
# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up
# or down. You may NOT move diagonally or move outside of the boundary
# (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# -------------------------------------------------------------------------
# Tagged as Memoization:

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memory = [[None] * len(matrix[0]) for i in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.helper(i, j, matrix, memory))

        return res

    def helper(self, i, j, matrix, memory):
        if memory[i][j]: return memory[i][j]
        count = 0
        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            count = max(count, self.helper(i - 1, j, matrix, memory))

        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            count = max(count, self.helper(i, j - 1, matrix, memory))

        if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
            count = max(count, self.helper(i + 1, j, matrix, memory))

        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
            count = max(count, self.helper(i, j + 1, matrix, memory))

        memory[i][j] = count + 1

        return count + 1

