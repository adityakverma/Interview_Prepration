
# Tags: Strings, DP, FB, MS, Uber
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# ...
# 'Z' -> 26
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# Example 1:
# Input: "12" # Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: "226" # Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if int(s[0]) == 0:
            return 0

        count = 0
        for i in range(len(s) - 1):
            num = int(s[i]) + int(s[i + 1])
            if num <= 26:
                count += 1
        return count + 1  # plus 1 because of one default way with all s[i] taken individually.

if __name__ == '__main__':
    input = "0" # "10"
    s = Solution()
    print "\nDecode ways:",s.numDecodings(input)


