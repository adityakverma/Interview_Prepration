
class Solution(object):

    # ---------------------------------------------------------------------------
    # THIS SEEM LIKE TABULATION METHOD OR BOTTOM UP METHOD.
    # NOTE: You MUST draw the tabulation table to understand and write this code below.
    # https://www.youtube.com/watch?v=_nCsPn7_OgI&index=9&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

    def LC_516_longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] # 2 + look diagonally left down which is row+1 and col-1. Note [0][0] is on left top.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) # if s[i] != s[j] then its either of inner groups which are already pre-computed.

        return dp[0][n - 1]
    # ---------------------------------------------------------------------------
    # A bottom-up solution
    def fib_bottom_up(self,n):
        if n == 1 or n == 2:
            return 1
        bottom_up = [None] * (n + 1)  # Initialise an empty array of size n+1
        bottom_up[1] = 1
        bottom_up[2] = 1
        for i in range(3, n + 1):
            bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
        return bottom_up[n]

    # A memoized solution OR Top-Down Approach
    def fib_2(self, n, memo):
        if memo[n] is not None:
            return memo[n]
        if n == 1 or n == 2:
            result = 1
        else:
            result = self.fib_2(n - 1, memo) + self.fib_2(n - 2, memo)
        memo[
            n] = result  # Update solutions to sub-problems in end, which can be used later to check. If solution to subproblem is already present then just reuse it.
        return result

    def fib_memo(self,n):
        memo = [None] * (n + 1)
        return self.fib_2(n, memo)

    # ---------------------------------------------------------------------------
    # def maxSubArray2(self, nums): # Without DP
    #     for i in range(1, len(nums)):
    #         nums[i] = max(nums[i - 1]+ nums[i], nums[i])
    #     return max(nums)

    def LC_053_maxSubArray(self, nums):

        if not nums:
            return None

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    # ---------------------------------------------------------------------------


    # ---------------------------------------------------------------------------



#################################################################################

if __name__ == '__main__':
    s = Solution()
    str = "abhjba"
    print "\nLongest Palindrome Subsequence:",s.LC_516_longestPalindromeSubseq(str)
    print "Fibonnic series:",s.fib_bottom_up(6)
