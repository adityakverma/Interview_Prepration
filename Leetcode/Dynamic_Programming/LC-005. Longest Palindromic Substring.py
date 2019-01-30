


# Given a string s, find the longest palindromic substring in s. You may
# assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# ==========================================================================

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):

            # odd case, when result is like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            # even case, when result is like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

# ----------------------------------------------------------------------

# https://leetcode.com/problems/longest-palindromic-substring/discuss/157861/Python3-DP-Solution-with-Lots-of-Comments
# Also see LC 647, 516


