
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        N1 = len(p)
        N2 = len(s)
        dp = [[False for j in range(N2 +1)] for i in range(N1 +1)]
        for i in range(N1 +1):

            for j in range(N2 +1):
                if( i==0 and j== 0):
                    dp[i][j] = True

                elif (j == 0):
                    dp[i][j] = (N1 > 0 and i > 0 and p[i - 1] == '*' and (dp[i - 1][j]))
                elif (i == 0):
                    dp[i][j] = (N1 > 0 and i > 0 and p[i - 1] == '*' and (dp[i][j - 1]))

                else:
                    dp[i][j] = ((dp[i - 1][j - 1] and (N1 > 0 and N2 > 0 and p[i - 1] == s[j - 1])) or
                                (N1 > 0 and p[i - 1] == '*' and (dp[i - 1][j] or dp[i][j - 1])) or
                                (N1 > 0 and p[i - 1] == '?' and dp[i - 1][j - 1]))
        return dp[N1][N2]

        # Based on Tushar Roy: https://www.youtube.com/watch?v=3ZDZ-N0EPV0&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=25&t=26s
