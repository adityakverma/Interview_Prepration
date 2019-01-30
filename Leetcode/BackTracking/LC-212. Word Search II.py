
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be
# used more than once in a word.
#
# Example:
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
# ---------------------------------------------------------------------------------------

# Below got ACCEPTED, though above one is same concept but failing few testcases:

import collections

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root

        for w in words:
            trie.insert(w)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)

        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)

        if not node:
            return

        board[i][j] = "#"  # To avoid looping.   Backtracking
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp  # Putting back once recursive function does callback. Backtracking


























# --------------------------------------------------------------------------------------------

# https://leetcode.com/problems/word-search-ii/discuss/59905/Python-AC-solution

from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.flag = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.flag = True


class Solution():

    result = []
    def findWords(self, board, words):

        trie = Trie()
        root = trie.root

        # First we build the Trie
        for w in words:
            trie.insert(w)

        # Then we search for the all board elemets in Trie of words.
        # Note here we passed root of Trie instead of word (LC-79)
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(root, board, j, i)

        return self.result

    def dfs(self, node, board, j, i, word=''):

        if node.flag:   # If we found end flag, then append word to result.
            self.result.append(word)
            node.flag = False

        if 0 <= j < len(board) and 0 <= i < len(board[0]):
            char = board[j][i]
            child = node.children.get(char)

            if child is not None:
                word += char
                board[j][i] = None
                self.dfs(child, board, j + 1, i, word)
                self.dfs(child, board, j - 1, i, word)
                self.dfs(child, board, j, i + 1, word)
                self.dfs(child, board, j, i - 1, word)
                board[j][i] = char

if __name__ == '__main__':

    words = ["oath","pea","eat","rain"]
    board = [
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
            ]

    s1 = Solution()
    print "\nSolution : ", s1.findWords(board, words)

##########################################################################








