
# Given two words word1 and word2, find the minimum number of steps
# required to make word1 and word2 the same, where in each step you can
# delete one character in either string.
#
# Example 1: Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# --------------------------------------------------------------------------------------------


# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/143842/Python-DP-solution-beats-97

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103267/Python-Straightforward-with-Explanation

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/135088/Python-Solution-Beats-97
# https://github.com/BlakeBrown/LeetCode-Solutions/blob/master/583%20-%20Delete%20Operation%20for%20Two%20Strings.py

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/117834/Python-DP-320ms-solution-beats-100
# ----------------------------------------------------------------------------------------------

# Another Similar Problem: LC-712. Minimum ASCII Delete Sum for Two Strings:
# =======> https://leetcode.com/problems/delete-operation-for-two-strings/discuss/172029/Python-DP-solution-same-as-problem-712


# Very Simple Idea that the number of deletions is equal to the number of places where both strings are different.
# So simply find the longest common subsequence(alphabets common in both in the same order) and ​subtract it from
# both the strings to find the elements that have to be deleted
# Youtube Explanation for Longest Common Subsequence (Tushar Roy) : https://www.youtube.com/watch?v=NnD96abizww


# longest common subsequence DP solution

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        CommonSubseqLength = self.longestCommonSubSeq(word1, word2)
        return len(word1) + len(word2) - 2 * CommonSubseqLength

    def longestCommonSubSeq(self, s, t):
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

################################################################################
# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/202134/Python-Dynamic-Programming-and-space-optimization


# A naive dp method is easy to get, we calculate the longest common "substring" (no need to be consecutive)
# It costs O(n^2) time complexity and O(n^2) space complexity

class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0 for _ in xrange(len(word2) + 1)] for _ in xrange(len(word1) + 1)]

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return len(word1) + len(word2) - 2 * dp[-1][-1]

# Here we can optimize our dp method to reduce space cost by only using a list rather than a matrix
# Time complexity: O(n^2)
# Space complexity: O(n)

import copy

class Solution(object):
    def minDistance(self, word1, word2):
        dp = [0 for _ in xrange(len(word2) + 1)]

        for i in xrange(1, len(word1) + 1):
            tmp = copy.deepcopy(dp)
            for j in xrange(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    tmp[j] = dp[j - 1] + 1
                else:
                    tmp[j] = max(tmp[j - 1], dp[j])

            dp = tmp

        return len(word1) + len(word2) - 2 * dp[-1]



'''

Java DP Solution, same as Edit Distance

public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        if (len1 == 0) return len2;
        if (len2 == 0) return len1;

        // dp[i][j] stands for distance of first i chars of word1 and first j chars of word2
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i++)
            dp[i][0] = i;
        for (int j = 0; j <= len2; j++)
            dp[0][j] = j;

        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1), dp[i][j - 1] + 1);
            }
        }

        return dp[len1][len2];
    }
}


'''