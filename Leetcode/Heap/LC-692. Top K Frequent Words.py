
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two
#  words have the same frequency, then the word with the lower alphabetical
# order comes first.
#
# Example 1:
#
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.

# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# Means HEAP :)

# --------------------------------------------------------------------------

# Intuition and Algorithm
#
# Python O(nlogk) Time O(n) Space

from heapq import *
import collections

class Solution(object):

    # ---------------- Using HEAP and Counter -------------------
    def topKFrequent(self, words, k):

        if words is None or len(words) == 0:
            return []

        count = collections.Counter(words)
        heap = []
        result = []
        #print count.keys(), candidates, len(candidates)

        for key,value in count.items():
            heappush(heap,(-value,key))  # -ve value so we pop max frequent first.

        for _ in range(k):
            result.append(heappop(heap)[1])

        return result

    # ---------- Using Heap, but without using Counter ------------
    def topKFrequent_(self, words, k):

        if words is None or len(words) == 0:
            return []
        dict = {}
        PQ = []

        for word in words:
            dict[word] = dict.get(word,0) + 1 # dict.get(key, value) - Here key - key to be searched. value if the key is not found and value is specified.

        for key in dict:
            heappush(PQ, (-dict[key],key))

        return [heappop(PQ)[1] for _ in range(k)]


if __name__ == '__main__':

    Input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 2
    #Output: ["the", "is", "sunny", "day"]

    s = Solution()
    print "\nTop K frequent words:",s.topKFrequent(Input, k)

    print "\nTop K frequent words:",s.topKFrequent_(Input, k)










#######################################################################

'''
# Below solution uses TRIE - which is slow.

# This version is much slower.
# 
# Idea:
#     Build a word/freq mapping
#     Since the # of freq must less or equal than len(words), then we could adopt counting sort.
#     Using trie to iterate the anwsers

from collections import defaultdict, Counter

class TreeNode(object):
    def __init__(self):
        self.word = None
        self.children = [None] * 26

class Solution:
    def __init__(self):
        self.results = []

    def build_tries(self, word_list):
        root = TreeNode()
        for word in word_list:
            ptr = root
            for ch in word[:]:
                idx = ord(ch) - ord('a')
                if not ptr.children[idx]:
                    ptr.children[idx] = TreeNode()
                ptr = ptr.children[idx]
            ptr.word = word
        return root

    def get_words(self, node):
        if node.word and self.k:
            self.results.append(node.word)
            self.k -= 1
        for nd in node.children:
            if nd:
                self.get_words(nd)

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_counting = Counter(words)
        freq_mapping = []
        self.k = k
        self.restuls = []
        for i in range(len(words)):
            freq_mapping.append([])
        for word, freq in words_counting.items():
            freq_mapping[freq].append(word)
        for word_list in freq_mapping[::-1]:
            trie = self.build_tries(word_list)
            for i in trie.children:
                if i and self.k:
                    self.get_words(i)
        return self.results

'''