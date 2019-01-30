
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input:  "bbbab"
# Output: 4

# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99117/Python-standard-DP-beats-100-(with-%22pre-processing%22)
# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/157682/Python-DP

# THIS SEEM LIKE TABULATION METHOD OR BOTTOM UP METHOD.

from collections import defaultdict

# Looks Similar to LC 5 and 647. Also see

class Solution:

    # ------------------------------------------------------------------------
    # Bottom up approach - Tabulation ( of dp matrix). No recursion used, but we use loop for computation.

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] # 2 + look diagonally left down which is row+1 and col-1. Note [0][0] is on left top.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) # if s[i] != s[j] then its either of inner groups which were pre-computed.

        return dp[0][n - 1]

    # ------------------------------------------------------------------------
    # Top Down Approach - Using memoization during recrsive calls for keeping records for computed subproblems. Note results are saved in hash

    def helper(self, i, j, s, cache):
        if i > j:
            return 0
        elif i == j:
            return 1
        elif i in cache and j in cache[i]:
            return cache[i][j]

        elif s[i] == s[j]:
            cache[i][j] = self.helper(i + 1, j - 1, s, cache) + 2
            return cache[i][j]
        else:
            cache[i][j] = max(self.helper(i, j - 1, s, cache), self.helper(i + 1, j, s, cache))
            return cache[i][j]

    def longestPalindromeSubseq_TopDown(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = defaultdict(dict)
        return self.helper(0, len(s) - 1, s, cache)


if __name__ == '__main__':
    s = Solution()
    str = "abhjba"
    print s.longestPalindromeSubseq(str)



###################################################################################################

# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/216717/Python-DP-solution-w-explanation

# There is nothing unique about this solution since everyone and their moms knows this is a
# practical solution since the time complexity is O(n^2), but they don't really explain why
# it works, or what the bottom up table represents.
#
# What is really happening with DP solution is it follows a simple brute force approach, that
# it tries to find the longest palindrome substring w/ respect to the position of each character:
# For example: "BBBAB"

# We want to know the longest Palindrome from:
# BBBAB
# BBAB
# BAB
# AB
# B
#
# But notice, if you're viewing this backwards, B contains information that AB can use, and AB
# contains information that BAB can use, and indeed, true to the nature of DP, we can make use
# of information from previous calculations.
#
# The tricky part is representing this in a data structure for our memoization, and we'll go with
# an intial matrix to represent the example above:

# __B B B A B
# B 1
# B 0 1
# B 0 0 1
# A 0 0 0 1
# B 0 0 0 0 1
#
# So what the heck is happening here? Why ones and zeros? If you look at the table, it's quite
#  simple, If we're looking at our first B, from BBBAB, we obviously only have 1 palindrome so
# far, and that is "B" BBAB, and likewise, if we're looking at the first B on BBAB, then we have
# 1 so far as "B" BAB, and the B before BBAB, is set to zero because technically, true to our
# idea, if we're looking at BBAB, we shouldn't have any info about the B before BBAB.
#
# From then on we simply build our table with the following logic, if the current row character
# matches the column character, then we take value from row+1 and column-1, and increment by 2.
# Why? Suppose we have BCCCB, if we're looking BCCCB vs CCCB, BCCCB has a length of 5 that is a
# paldinrome, while CCCB has 3 (CCC), so the difference is 2.
#
# Also if you think about it, from the table's standpoint, row+1 and column-1 would represent CCC,
# since the current column char is B, while the next row's starting chair is "C" CC.
#
# If it doesn't match, then we take the max between the left value, and the bottom value of our
# current position. Why? Consider this, if we have BBA, and BA, we know that BBA has a value of 2,
# while BA is 1, so if we're looking at another character, say BBA "C" from the point of view of "B"
# BAC, then we still have a value of 2, while "B" AC is still 1.
#
# So if you fill the table, you'll eventually get the following:
# __B B B A B
# B 1 2 3 3 4
# B 0 1 2 2 3
# B 0 0 1 1 3
# A 0 0 0 1 1
# B 0 0 0 0 1
#
# We are actually going to traverse the table diagonally since that's the only way to fill the table
# in a way that we can access information from the [row+1, column-1], [row+1, column], [row, column-1]

# ============================================================================================



