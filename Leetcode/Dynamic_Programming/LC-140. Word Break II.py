
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.

# Note:
#
#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.
#
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# ------------------------------------------------------------------------------


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            # print word, s
            if not s.startswith(word):
                # print "...."
                continue
            if len(word) == len(s):
                # print "Equal length", word, s
                res.append(word)
                # print "Equal Res", res
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                # print "resultOfTheRest", resultOfTheRest
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

    # https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
    # https://leetcode.com/problems/word-break-ii/discuss/194615/DP-solution-with-detailed-text-and-video-explanation
    # Need to understand

