
# Tags: Hash table, String, Tries, Google, airbnb

# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
# Example 2:
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# https://leetcode.com/problems/palindrome-pairs/description/
# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

class TrieNode():
    def __init__(self):
        self.children = {}
        self.indexes = []
        self.index = -1

class Solution:

    # ---------------- Using TRIE ---------------------------
    # https://leetcode.com/problems/palindrome-pairs/discuss/130811/Python3-Trie-solution-can-anyone-help-me-improve-my-code

    def palindromePairs_usingTrie(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # check if a string is palindrome
        def isValid(s):
            p0, p1 = 0, len(s) - 1
            while p0 < p1:
                if s[p0] != s[p1]:
                    return False
                p0 += 1
                p1 -= 1
            return True

        # add word and if it's not the end, add to the indexes, else index

        def addWord(word, i):
            node = root
            for j in range(len(word) - 1, -1, -1): # Note: Creating Trie for reversed word
                if word[j] not in node.children:
                    node.children[word[j]] = TrieNode()
                node = node.children[word[j]]

                # I store the index into indexes when it's only part of word
                if j > 0 and isValid(word[:j]): # As its building Trie for that word. Its also checking for itself, if its part is a palindrome, then save those indexes.
                    node.indexes.append(i)
                    print "Valid", j, word[:j], node.indexes

            node.index = i
            print "Added: ", word, node.index, node.indexes

        # check if this word can be palindrome pair with other word
        # we can only use (part of a + b) or (a + part of b) or (a + b) not (part of a + part of b)
        # Aditya: example lls which we added as sll . And when checked with 's' for its like (a + part of b)
        def checkWord(word, i):
            node = root
            #if node.index >= 0 and isValid(word) and i != node.index:
                #ans.append((node.index, i))
                #ans.append((i, node.index))
            print "\ncheckWord", word, node.index
            for j in range(len(word)):
                if word[j] not in node.children:
                    return
                else:
                    node = node.children[word[j]]
                    print "Debug: index", node.index, i, word[j], j, word[j+1:]

                    # node.index >= 0 means its a valid complete word from given list
                    # node.index != i means its not itself.
                    # isValid(word[j + 1:]) means Its palindrome for remaining
                    if node.index >= 0 and node.index != i and isValid(word[j + 1:]):
                        ans.append((i, node.index))
                        print "Appended index of complete ones: ",i,node.index

            #print "ii", i
            for j in node.indexes:
                #print "Adding partials one....", j
                if i != j:
                    ans.append((i, j))
                    print "\nAppended index of Partial ones",i, j

        # build our Trie and check for each word
        root = TrieNode()
        ans = []

        for i, j in enumerate(words):
            print "\nCalling addword for", i, j
            addWord(j, i)

        print "#####################################"
        for i, j in enumerate(words):
            checkWord(j, i)
        return ans

    # -------------- Without using TRIE, but O(N^2) -----------------------
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        if len(words) == 0:
            return []
        output = []

        for i in range(len(words)):
            for j in range(len(words)):

                if words[i] != words[j]:
                    concat_w = words[i] + words[j]
                    if concat_w == concat_w[::-1]:
                        output.append([i, j])
        return output
    # -----------------------------------------------------------------------

if __name__ == '__main__':

    input = ["abcd","dcba","lls","s","sssll"]
    s = Solution()

    print "\nPairs are:",s.palindromePairs(input)

    print "\nPairs are:",s.palindromePairs_usingTrie(input)