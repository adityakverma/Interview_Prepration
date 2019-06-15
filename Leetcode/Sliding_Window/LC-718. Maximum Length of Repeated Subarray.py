

# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
# ================================================================================================

# THIS IS DP Question:

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):

                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        return max(max(row) for row in dp)

        # https://www.youtube.com/watch?v=BysNXJHzCEs
        # Longest Common Substring - Uses DP technique. Super Easy problem

# ======================================================================================================


