
# Tags: Hash Table, Tries, Google

#  Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
#
# Example 1:
#
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
# Note:
#
#  You may assume that all the inputs are consist of lowercase letters a-z.
#  For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
#  Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
# ---------------------------------------------------------------------------------------------

# The basic idea here is very simple: we construct a dictionary, whose key is the length of
# the given words, and the value is a list containing the words with the same length specified
# in the key. And when we search a word (say word "hello") in the magic dictionary, we only
# need to check those words in dic[len("hellow")], ( named candi in my code).

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in words:
            self.dict[len(i)] = self.dict.get(len(i), []) + [i]
        print self.dict.items()

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candi in self.dict.get(len(word), []): # Looking for all words of that list which have same length as len(word)
            countdiff = 0
            for j in range(len(word)):
                if candi[j] != word[j]: # Simple match of each characters.
                    countdiff += 1
            if countdiff == 1:
                return True
        return False


# Approach #1: Brute Force with Bucket-By-Length [Accepted]
#
# Intuition and Algorithm
# -----------------------
# Call two strings neighbors if exactly one character can be changed in one to make the
# strings equal (ie. their hamming distance is 1.)

# Strings can only be neighbors if their lengths are equal. When searching a new word,
# let's check only the words that are the same length.
#
# Python
#
# class MagicDictionary(object):
#     def __init__(self):
#         self.buckets = collections.defaultdict(list)
#
#     def buildDict(self, words):
#         for word in words:
#             self.buckets[len(word)].append(word)
#
#     def search(self, word):
#         return any(sum(a!=b for a,b in zip(word, candidate)) == 1
#                    for candidate in self.buckets[len(word)])



# https://leetcode.com/problems/implement-magic-dictionary/solution/#


