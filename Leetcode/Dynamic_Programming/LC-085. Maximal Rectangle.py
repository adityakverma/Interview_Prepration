

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
# -------------------------------------------------------------------------

class Solution(object): # ACCEPTED

    # The solution is based on largest rectangle in histogram solution. Every row in the matrix is viewed as the ground with some
    # buildings on it. The building height is the count of consecutive 1s from that row to above rows. The rest is then the same as
    # this solution for largest rectangle in histogram

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        height = [0] * (
        n + 1)  # DP Array, which we update for each row of input matrix. Note we do n+1 because see LC-84
        ans = 0

        for row in matrix:

            # Update height array for current row based on previous row's height array [dp] and input matrix. This was input in LC-084
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            # Now below is way to find max rectangle in histogram. LC-084
            # The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the
            # building who is taller than the new one. The building popped out represent the height of a rectangle with
            # the new building as the right boundary and the current stack top as the left boundary. Calculate its area
            # and update ans of maximum area. Boundary is handled using dummy buildings.

            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)

        return ans
