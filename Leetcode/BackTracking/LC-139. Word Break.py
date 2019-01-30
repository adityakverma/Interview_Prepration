

######### THIS IS NOT BACKTRACKING. I USED DP HERE #################

# https://leetcode.com/problems/word-break/discuss/44009/Concise-Python-DP-solution
# https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution

class Solution(object):

    # https://leetcode.com/problems/word-break/discuss/44009/Concise-Python-DP-solution
    def wordBreak(self, s, wordDict):

        n = len(s)
        dp = [False] * (n+1) # dp is an array that contains booleans
        dp[0] = True

        for i in xrange(1,n+1):
            for j in xrange(0,i):       # Seems like Kadane where we check previous precomputed results stored at is_breakable[i]
                if dp[j] and s[j:i] in wordDict:
                    #print "(i,j)",i,j, s[j:i], dp[j]
                    print s[j:i], i, j
                    dp[i] = True # dp[i] is True if dp[j] was found before in worddict from past computation. And remaining word is also present in dict.
                    break

        #print dp
        return dp[-1] # Last should be True, menaing whole string is breakable


    # ====================================================

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True

        for i in range(len(s)):
            for j in range(i, len(s)):

                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True

        return dp[-1] # Last should be True, menaing whole string is breakable

if __name__ == '__main__':
    str = "applepenapple"
    wordDict = ["apple", "pen"]
    s = Solution()
    print s.wordBreak(str,wordDict)

# Implement same issue using Trie
# https://www.geeksforgeeks.org/word-break-problem-trie-solution/

# ---------------------------------------------------------------------------------------

# # The idea is the following:
#
#     d is an array that contains booleans
#
#     d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word
#
# Example:
#
#     s = "leetcode"
#
#     words = ["leet", "code"]
#
#     d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
#
#     d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
#
