
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
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
#
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# -------------------------------------------------------------------------------------------

# This is same Word Search problem
# DP: Here we doing DP/ memoization because once we know the path - so we know how many more
# ( increasing lower) from any specific cell can be found if again come to that cell in future,
# so we don't need to again do DFS for that cell.

# Time complexity : O(M*N) where M is rows, N is column. this is with memoization
#                   Without memoization time complexity would have been (M*N)^2 because then
#                   we will visit each cell twice and scan evrytime every neighbour twice

# Space Complexity: O(1) without memoization
#                   O(M*N) with memoization because we need extra matrix to save results for DP.


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

if __name__ == '__main__':
    nums = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
         ]
    s = Solution()
    print "\nLongest path ", s.longestIncreasingPath(nums)

# =================== ACCEPTED =================================

