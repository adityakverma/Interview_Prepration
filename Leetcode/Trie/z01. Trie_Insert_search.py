
# https://www.geeksforgeeks.org/trie-insert-and-search/
# https://www.geeksforgeeks.org/trie-display-content/


# Python program for insert and search
# operation in a Trie

class TrieNode:
    # Trie node class
    # Every node of Trie consists of multiple branches. Each branch represents a possible
    # character of keys. We need to mark the last node of every key as end of word node.
    # A Trie node field isEndOfWord is used to distinguish the node as end of word node.
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            print key, length, index

            # if current character is not present
            if not pCrawl.children[index]:
                print "..", index, pCrawl.children[index]
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

# The following picture explains construction of trie using keys given in the example below,
#
#                        root
#                     /   \    \
#                     t   a     b
#                     |   |     |
#                     h   n     y
#                     |   |  \  |
#                     e   s  y  e
#                  /  |   |
#                  i  r   w
#                  |  |   |
#                  r  e   e
#                         |
#                         r

# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "bbb", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
    print("{} ---- {}".format("bbb", output[t.search("bbb")]))



if __name__ == '__main__':
    main()

