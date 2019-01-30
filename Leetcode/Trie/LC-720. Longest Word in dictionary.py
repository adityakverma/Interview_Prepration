
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
# If there is no answer, return the empty string.
#
# Example 1:
#
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# ---------------------------------------------------------------------------------------

# Approach: Trie + Depth-First Search [Accepted]

# Complexity Analysis
#
#  Time Complexity: O(Sum of Wi) where Wi is the length of words[i]. This is the
#  complexity to build the trie and to search it.
#
# If we used a BFS instead of a DFS, and ordered the children in an array, we could drop the
# need to check whether the candidate word at each node is better than the answer, by forcing
# that the last node visited will be the best answer.
#
#     Space Complexity: ***, the space used by our trie.
# -------------------------

import collections

class TrieNode(object):
    def __init__(self):
        self.children =collections.defaultdict(TrieNode)
        self.isEnd =False
        self.word =''

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # Step 1: Construct a trie
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True  # Important - Marks end of Word in Trie.
        node.word = word   # Important - Places whole word here, once it sees isEnd=True

    # Step 2: Find longest word with DFS
    def bfs(self):
        q = collections.deque([self.root])
        res = ''

        while q:
            cur = q.popleft()
            for n in cur.children.values(): # n is node

                if n.isEnd: # you reached end of that word. So two things. Append it to queue AND check the length iof n.word if its greater than res then assign it.
                    q.append(n)
                    if len(n.word) > len(res): #or n.word < res:
                        res = n.word
        return res

class Solution(object):
    def longestWord(self, words):
        trie = Trie()
        for w in words: trie.insert(w)
        return trie.bfs()


if __name__ == '__main__':
    pass

    s = Solution()
    words = ["w","wo","wor","worl", "world"]
    print "\nLongest Word is :",s.longestWord(words)


# Hi, I have a basic question, so only the leaf node (ending letter of a complete word) stores the entire word in node.word right?
