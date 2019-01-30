# Tags: Tries, Google, MS, Backtracking,
# https://www.geeksforgeeks.org/word-break-problem-trie-solution/
# https://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/

# Another Problem:
# https://www.geeksforgeeks.org/pattern-searching-using-trie-suffixes/
# https://leetcode.com/problems/word-search-ii/discuss/59905/Python-AC-solution

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

####################################################################

from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.flag = False

class Solution():

    #----------------------------------------------

    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.flag = True
    #----------------------------------------------

    def findWords(self, board, words):
        for w in words:
            self.insert(w)  # Make a Trie for each word in list.

        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(self.root, board, j, i)
        return self.result

    # [Aditya]: So basically in this dfs function, we picked the character from board and seeing if it's
    # in Trie's child (not none). If not none then look for next char from board and see if that
    # also matches with next child within Trie and so on. While doing this, keep checking if flag
    # is set for that word (created so far via appending). If flag is set or true, that means word
    # from trie is present in board, so append that valid word to result list

    def dfs(self, node, board, j, i, word=''):
        
        if node.flag:
            self.result.append(word)
            node.flag = False

        if 0 <= j < len(board) and 0 <= i < len(board[0]):

            char = board[j][i]   # Pick the char from board[][] AND check that char in Trie which we have build. If its non none , meaning char from board is present in board, then keep looking for other via DFS
            child = node.children.get(char)  # So basically we picked the character from board and seeing if it's in Trie's child (not none). If not None ( meaning its present) then look for next char from board and see if that also matches with next child within Trie and so on.

            #print "child", char, child
            if child is not None:
                #print child, char
                word += char
                #print ".....",word

                board[j][i] = None  # Since as per problem, letters may not be used more than once in a word.
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
