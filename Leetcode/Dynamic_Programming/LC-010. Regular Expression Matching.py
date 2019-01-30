
# Given an input string (s) and a pattern (p), implement regular expression
#  matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters
# like . or *.
#
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by
# repeating 'a' once, it becomes "aa".
#
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#################################################################################


class Solution:
    def isMatch(self, s, p):

        # ----------------------------------------------------------------------
        # Without DP:

        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        # ----------------------------------------------------------------------

    def isMatch_DP(self, s, p):

        # DP solution w.r.t Tushar Roy's video https://www.youtube.com/watch?v=l3hda49XcDE&t=14s
        # https://leetcode.com/problems/regular-expression-matching/discuss/182669/Easy-10-line-DP-Python-solution-with-explanation

        m = len(s)
        n = len(p)
        dp = [[False for i in range(n+1)] for j in range(m+1)] # dp[i][j] stores the result of isMatch(s[:i], p[:j])
        dp[0][0] = True # s[:0] = '', p[:0] = '', isMatch("","") is True

        for i in range(2,n+1): # corner case: '' can match with expressions like 'a*b*c*.*'
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        for i in range(1,m+1):
            for j in range(1,n+1):

                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
                else:   # current pattern p[j-1] is '*', we need to know the preceding element p[j-2]
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j])

        return dp[m][n]

        # ----------------------------------------------------------------------

        # Time and Space Complexity are same which is O(m*n)

# The difference is that: the * in this problem can match any sequence independently, while the * in Regex Matching would only match duplicates, if any, of the character prior to it.
#
# The demo test case isMatch("aa", "*") for this problem and isMatch("aa", "a*") for Regex Matching problem could be the best effort to distinguish them for now. isMatch("aab", "c*a*b") → false for this problem was a bit confusing to me in the beginning. I think adding a test case such as isMatch("adcab", "*a*b") → true might be helpful.


'''
import unittest


class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        print "HERE////"
        self.assertTrue(Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))


if __name__ == "__main__":

    #unittest.main()
    t = TestSolution()
    print "OK.........."
    print t.test_symbol_1()
    
    '''
    
    