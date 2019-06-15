
import unittest


class Solution(object):
    def isMatch(self, s, p):

        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for j in
              range(m + 1)]  # dp[i][j] stores the result of isMatch(s[:i], p[:j])
        dp[0][0] = True  # s[:0] = '', p[:0] = '', isMatch("","") is True

        for i in range(2, n + 1):  # corner case: '' can match with expressions like 'a*b*c*.*'
            dp[0][i] = dp[0][i - 2] and p[i - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                else:  # current pattern p[j-1] is '*', we need to know the preceding element p[j-2]
                    dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])

        return dp[m][n]


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
    unittest.main()


# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest/222796

# This looks like python2. As long as you have python2 on your machine, you should be able to:
#
#     Copy/paste this into a file (call it test.py or whatever you want)
#     Run python2.7 test.py
#     And the output should look like:
#
# $ python test.py
#
# ........
# ----------------------------------------------------------------------
# Ran 8 tests in 0.001s
#
# OK
#
# You can make unittest run with higher verbosity from command line with something like:
# $ python -m unittest -v test
#
# test_no_symbol_equal (test.TestSolution) ... ok
# test_no_symbol_not_equal_0 (test.TestSolution) ... ok
# test_no_symbol_not_equal_1 (test.TestSolution) ... ok
# test_none_0 (test.TestSolution) ... ok
# test_none_1 (test.TestSolution) ... ok
# test_symbol_0 (test.TestSolution) ... ok
# test_symbol_1 (test.TestSolution) ... ok
# test_symbol_2 (test.TestSolution) ... ok
#
# ----------------------------------------------------------------------
# Ran 8 tests in 0.001s
#
# OK

