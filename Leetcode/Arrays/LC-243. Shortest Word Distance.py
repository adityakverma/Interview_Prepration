
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
#
# Input: word1 = "makes", word2 = "coding"
# Output: 1
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# ==============================================================================================

# This is a straight-forward coding problem. The distance between any two positions i1i_1i1​ and i2i_2i2​ in an
# array is ∣i1−i2∣|i_1 - i_2|∣i1​−i2​∣. To find the shortest distance between word1 and word2, we need to traverse
# the input array and find all occurrences i1i_1i1​ and i2i_2i2​ of the two words, and check if ∣i1−i2∣|i_1 - i_2|∣i1​−i2​∣ is
# less than the minimum distance computed so far.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1, index2 = size, size
        ans = size

        for i in xrange(size):
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1 - index2))
            elif words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1 - index2))
        return ans

        # O(n) time, O(1) space