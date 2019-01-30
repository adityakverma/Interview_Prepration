
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated sequence
# of one or more dictionary words.

# Note:

#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.
#
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# ======================================================================================

class Solution(object):

    # https://leetcode.com/problems/word-break/discuss/44009/Concise-Python-DP-solution
    def wordBreak(self, s, wordDict):

        n = len(s)
        dp = [False] * (n+1) # dp is an array that contains booleans
        dp[0] = True  # This helps to get first matchable string from wordDict with given 'if' condition below.

        for i in xrange(1,n+1):
            for j in xrange(0,i):       # Seems like Kadane where we check previous precomputed results stored at is_breakable[i]

                if dp[j] and s[j:i] in wordDict:
                    # print s[j:i], i, j
                    dp[i] = True # dp[i] is True if dp[j] was found before in worddict from past computation. And remaining word is also present in dict.
                    break # Breaks from immediate for loop. Not all for loops.
        #print dp
        return dp[-1] # Last should be True, meanaing whole string is breakable





if __name__ == '__main__':
    str = "applepenapple"
    wordDict = ["apple", "pen"]
    s = Solution()
    print s.wordBreak(str, wordDict)

# Example:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# apple 5 0
# pen 8 5
# apple 13 8
# ======================================================================================
