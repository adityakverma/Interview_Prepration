
# 245. Shortest Word Distance III

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
#
# Input: word1 = "makes", word2 = "makes"
# Output: 3
#
# Note:
# You may assume word1 and word2 are both in the list.
#
# =====================================================================================

# Just copy pasted

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        res = float('inf')
        i1, i2 = float('-inf'), float('-inf')

        for i, word in enumerate(words):
            if word == word1:
                if word1 == word2:
                    res = min(res, i - i1)  # this is for same word
                else:
                    res = min(res, i - i2)
                i1 = i
            elif word == word2:
                res = min(res, i - i1)
                i2 = i

        return res


