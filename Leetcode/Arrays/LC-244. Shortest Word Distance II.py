
# 244. Shortest Word Distance II

# Design a class which receives a list of words in the constructor, and implements a method that
# takes two words word1 and word2 and return the shortest distance between these two words in the list.
# Your method will be called repeatedly many times with different parameters.
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


class WordDistance(object):
    import collections

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        print self.d.items()
        l1 = self.d[word1]
        l2 = self.d[word2]
        print l1, l2
        i, j = 0, 0
        shortest = sys.maxint
        while i < len(l1) and j < len(l2):
            shortest = min(shortest, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return shortest


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

#--------------------------
# Your input

# ["WordDistance","shortest","shortest"]
# [[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]
#
# Your stdout
#
# [(u'perfect', [2]), (u'coding', [3]), (u'practice', [0]), (u'makes', [1, 4])]
# [3] [0]
# [(u'perfect', [2]), (u'coding', [3]), (u'practice', [0]), (u'makes', [1, 4])]
# [1, 4] [3]
#
# Your answer
#
# [null,3,1]
#
# Expected answer
#
# [null,3,1]



# Time Complexity: O(m+n)

#######################################################

class WordDistance_(object):


    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dw = {}
        for i, w in enumerate(words):
            if w in self.dw.keys():
                self.dw[w].append(i)
            else:
                self.dw[w] = [i]


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(i - j) for i in self.dw[word1] for j in self.dw[word2])


############################################################

class Word_Distance_(object):

    def __init__(self, words):
        self.dic, self.l = {}, len(words)
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i]

    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    # Adds a word into the data structure.
    def shortest(self, word1, word2):
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        res = self.l
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res