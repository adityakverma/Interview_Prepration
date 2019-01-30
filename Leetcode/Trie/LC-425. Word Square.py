
# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same
# string, where 0 <= k <= max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because
# each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y

####################################################################################
import collections

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        m = len(words)
        n = len(words[0]) if m else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        matrix = []
        ans = []
        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1)
            matrix.pop()
        for word in words:
            search(word, 1)
        return ans

# http://massivealgorithms.blogspot.com/2016/10/leetcode-425-word-squares.html


