
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#     Insert a character
#     Delete a character
#     Replace a character
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# ---------------------------------------------------------------------------

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):

                # build base case: what happens if one of prefixes is zero
                # (1) word1 prefix is empty, then keep adding
                dp[0][j] = j

                # (2) word2 prefix is empty, then keep deleting
                dp[i][0] = i

                if word1[i - 1] == word2[j - 1]:  # If letter is same, then no change, so copy previous result from uppper left diagonal
                    dp[i][j] = dp[i - 1][j - 1]

                else:  # Else we need some operation, so we take min of surrounding + 1. Checkout video on how we gotthis formula.

                    # dp[i-1][j-1] -> replace
                    # dp[i][j-1] -> add
                    # dp[i-1][j] -> delete
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[m][n]  # or dp[-1][-1]

        # https://www.youtube.com/watch?v=We3YDTzNXEk

        # https://leetcode.com/problems/edit-distance/discuss/193758/Java-and-Python-DP-Solutions:-Suffix-and-Prefix-implementations
