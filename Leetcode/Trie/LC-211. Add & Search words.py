

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
#
# search(word) can search a literal word or a regular expression string containing
# only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# ---------------------------------------------------------------------------

# Tags: Design, Tries, FB

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        # Initialize your data structure here.
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])




'''            
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
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
        node.word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word


if __name__ == '__main__':

    t = Trie()
    arr = ["I","work","at","Oracle","in","SantaClara"]

    for i in range(len(arr)):
        t.insert(arr[i])
    print "\nIs word present?",t.search("Oracle")
'''