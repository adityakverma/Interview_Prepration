# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58953/AC-Python-solution-using-defaultdict
from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Easy to insert new node.
        self.isword = False  # True for the end of the trie.

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isword = True

    # Returns TRUE if the word is in the trie, else FALSE.
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isword

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == '__main__':

    obj = Trie()
    obj.insert("AAA")
    print "\nFound -",obj.search("AAA")
    print "\nStartswith -",obj.startsWith("AAA")


#
# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             node = node.children[c]
#         node.is_word = True
#
#     def search(self, word, is_word=True):
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return node.is_word if is_word else True
#
#     def startsWith(self, prefix):
#         return self.search(prefix, False)


