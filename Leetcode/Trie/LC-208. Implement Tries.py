
# Tags: Design, Trie, FB, MS , google, Bloomberg, Uber
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58989/My-python-solution
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/111445/Easy-to-understand-basic-trie-in-Python

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    #-------------------------------------------------------------------------
    def insert(self, word):                 # INSERT
        print "Inserting ",word
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()   # Create new node for next alphabet of word, and move on.  Same as search, Here we just insert
            node = node.children[i]             # Its like p = p->next; Moving to next.
        node.word = True

    #-------------------------------------------------------------------------
    # Returns True if the word is in the trie.
    def search(self, word):                 # SEARCH
        print "\nSearching", word
        node = self.root
        for i in word:
            if i not in node.children:
                return False                # Same as Insert, here we just return False
            node = node.children[i]
        return node.word

    #-------------------------------------------------------------------------
    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix):           # Same as SEARCH ...
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

    #-------------------------------------------------------------------------
    # All below doesn't work well
    def isLeafNode(self,node):
        print node.word
        return node.word != False

    #-------------------------------------------------------------------------
    def display(self):
        node = self.root
        str = " "
        level = 0
        self.displayHelp(node,str,level)

    def displayHelp(self,node,str,level):

        if self.isLeafNode(node):
            print "....::",str

        for i in range(26):
            letter = chr(ord('a') + i)
            if letter in node.children:
                print "........", letter
                str = str+letter
                node = node.children
                print "...............",str
                #str[level] += `letter`
                self.displayHelp(node, str,level+1)

# Your Trie object will be instantiated and called as such:

# driver function
if __name__ == '__main__':

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "bbb", "there", "anaswe", "any",
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


    ###############
    # Test-2
    print "\n++++++++++++++++++++++++"
    t.insert("Aditya")

    print "\nSearch: ", output[t.search("Aditya")]
    print "\nStartWith: ", t.startsWith("Adi")

    print "\n++++++++++++++++++++++++\n"
    #t.display()









