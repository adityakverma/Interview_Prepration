# Tries is mainly used for word validation.
# Example 1: find all those words in list which are present in scramble board. Similar to LC-212
# Example 2: Given list of strings (sentences), find all celebrity names. Similar to this
# Example 3: My thought, underline word (just like in MS Word), if someone types word which isn't
# valid word (meaning not present in Trie tree). This is spelling check
# Example 4: Trie is ideal data structure for storing our Dictionary. Or Prefix based search.

# https://www.geeksforgeeks.org/word-break-problem-trie-solution/
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:
#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.
#
# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# --------------------------------------------------------------------------

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isWord = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.isWord

    #----------------------------------------------------

    # We first check whether current prefix is in dictionary. Then we
    # recursively check for remaining string s[i:len(s)] which is suffix 
    # of length size-i

    def wordBreak(self, s):
        if len(s) == 0:
            return True
        
        for i in range(1,len(s)+1): # Reason you need to do till len(s)+1 because in slicing we consider till one letter before in s[0:i]. So we'll never get last word. eg: google will always be googl if its s[0:i]
            #print "1st",s[0:i], "2nd",s[i:len(s)]
            if self.search(s[0:i]) and self.wordBreak(s[i:len(s)]):
                return True
        return False # If we have tried all prefixes and none of them worked

if __name__ == '__main__':

    t = Trie()
    arr = ["I", "work","at","Google","California"]

    for i in range(len(arr)):
        t.insert(arr[i])

    print "\nI work at Google ?", t.wordBreak("IworkatGoogle")
    print "I work at Oracle ?", t.wordBreak("IworkatOracle")
