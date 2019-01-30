
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, n):
            if int(s[i]) > 0:
                dp[i + 1] = dp[i]

            if int(s[i - 1:i + 1]) <= 26 and int(s[i - 1:i + 1]) > 9:
                dp[i + 1] += dp[i - 1]

        return dp[n]


    # Example 1: if we have 24 so we consider dp[0]=1 and dp[1] = 1 so here starting i from 1;
    # no of ways for element 2 is dp[i-1] = dp[0] = 1 and then looping to next element
    # 4 so we get dp[i-1] which is again 1 ( value for 2) plus if its (previous and itself )
    # meaning 24 is with 9-26 then add dp[i-1] too;
    # which means 1 (for2)+ 1 (for 0) so total is 2.

    # Example 2: 1224, so here dp[0] = 1 and we start from dp[1] = 1 so for i = 2 its s[i-1] = 1 + for 12 its 1 so total for 12 = 1+1=2 .
    # then moving to second 2. dp[2] = dp [previous] = 2 + for 22 which is in range 9-26 so s[i-1] which is for posotopn of 1 whose value
    # for dp[1] was 1, so total = 2+1 = 3. Next moving to 4, so we directly get s[i-1] which is 3 + for 24 its in range 9-26 so add dp[2]
    # which was 2 sp total 3+2 = 5 is answer

