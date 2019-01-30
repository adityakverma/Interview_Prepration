
#  There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules
# of this new language. Derive the order of letters in this language.

# Example 1:
# Given the following words in dictionary,
# 
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# 
# The correct order is: "wertf".
# Example 2:
# Given the following words in dictionary,
# 
# [
#   "z",
#   "x"
# ]
# 
# The correct order is: "zx".
# Example 3:
# Given the following words in dictionary,
# 
# [
#   "z",
#   "x",
#   "z"
# ]
# 
# The order is invalid, so return "".
# Note:
# 
#     You may assume all letters are in lowercase.
#     You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
#     If the order is invalid, return an empty string.
#     There may be multiple valid order of letters, return any one of them is fine.
# 
# ==================================================================================

# Thought process:
# Topological sort:
# 
#     Build graph: 
#         a map of character -> set of character.
#         Also get in-degrees for each character. In-degrees will be a map of character -> integer.
#     Topological sort:
#         Loop through in-degrees. Offer the characters with in-degree of 0 to queue.
#         While queue is not empty:
#             Poll from queue. Append to character to result string.
#             Decrease the in-degree of polled character's children by 1.
#             If any child's in-degree decreases to 0, offer it to queue.
#         At last, if result string's length is less than the number of vertices, that means there is a cycle in my graph. The order is invalid.

# ==================================================================================



'''

Solution

Alien Dictionary https://leetcode.com/problems/alien-dictionary/

Topological Sort Based Solution

Synoposis

    The basic idea behind this problem is simple. Build a graph from the dictionary of words. Then do a topological sort of the words. The meat is in the details and corner cases.

Meaning of Lexicographically Smaller

    Understanding what lexicographically smaller really means. Notice that adjacent words in the dictionary dictate the order. Letters within the word do not determine the lexicographic order. https://discuss.leetcode.com/topic/22395/the-description-is-wrong

Building an Input Graph

    Graph is a dictionary with key as character and edge end points as a set
    Every adjacent pair of word is extracted. All their characters are added to a graph as keys
    Now every adjacent character is compared. The first non-matching character determines a relationship u -> v and is added to graph. We break at this point since the remainder mis-matches do not imply any relationship.
    Notice a pair like ("wrtkj","wrt") - > this indicates no relationship since wrt match and then the smaller word is actually longer length than bigger word. This needs to be reported as an error.
    build_graph method returns the graph. If an error is found, empty graph is returned.

Topological Sort

    DFS or BFS can be used to implement topological sort. We use DFS.
    We run topological sort on each vertex.
    Topological sort requires a directed acyclic graph. If there is a cycle, we return True.
    How do we detect a cycle? We use the concept of back-edges. We maintain a visiting and visited array.
    Topological sort can be implemented using BFS as well. https://www.youtube.com/watch?v=71eHuQvSwc0

Interesting Examples

    ["wrtkj","wrt"] # Incorrect input
    ["a","b","a"] # Cycle
    ["wnlb"]

class Solution(object):
    def add_vertices(self, w, graph):
        for ch in w:
            if ch not in graph:
                graph[ch] = set([])
        return

    def add_words_to_graph(self, graph, w1, w2):
        self.add_vertices(w1, graph)
        self.add_vertices(w2, graph)
        min_length = min(len(w1), len(w2))
        found = False
        for i in range(min_length):
            if w1[i] != w2[i]:
                graph[w1[i]].add(w2[i])
                found = True
                break
        if found == False and len(w1) > len(w2):
            return False # "abstract", "abs" is an error. But "abs", "abstract" is perfectly fine.
        return True

    def build_graph(self, words):
        graph = {}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not self.add_words_to_graph(graph, w1, w2):
                return {}
        self.add_vertices(words[-1], graph)
        return graph

    def topo_dfs(self, x, g, visited, visiting, st): # Return True if there is a cycle
        visited.add(x)
        visiting.add(x)
        for nbr in g[x]:
            if nbr in visiting: # Back-Edge!
                return True
            if nbr not in visited:
                if self.topo_dfs(nbr, g, visited, visiting, st):
                    return True
        visiting.remove(x)
        st.append(x)
        return False

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == []:
            return ""
        graph = self.build_graph(words)
        visited, visiting, st = set([]), set([]), []
        for k in graph.keys():
            if k not in visited:
                if self.topo_dfs(k, graph, visited, visiting, st):
                    return ""
        st.reverse()
        return "".join(st)


Thanks for your explanations. However, I still confuse about this "Now every adjacent character is compared. The first non-matching character determines a relationship u -> v and is added to graph. We break at this point since the remainder mis-matches do not imply any relationship." Do you mind to talk more detail about this? Why do you use break after first mismactch?
No the OP. When comparing two words, the first non-matching character is the one which will set the order.

e.g.) Using English as the Alien Dictionary:
class
crane

"l" is before "r" in the alphabet, so "class" is place before "crane". If we didn't break we would compare "s" and "n" and wrongly label n as coming after "s". So the order after "l" doesn't matter.


'''

'''
We do not need a DFS or BFS to detect if there is a cycle, because if the graph stop shrinking before all nodes are removed, it indicates that solution doesn't exist (a cycle in the graph)
Python topological sort w/o BFS/GFS


class Node(object):
def __init__(self):
    self.IN = set()
    self.OUT = set()

class Solution(object):
def alienOrder(self, words):
   # find out nodes
   graph = {}
    for word in words:
        for letter in word:
            if letter not in graph:
                graph[letter] = Node()

    # find out directed edges (from StefanPochmann)
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                graph[a].OUT.add(b)
                graph[b].IN.add(a)
                break

    # topo-sort
    res = ""
    while graph:
        oldlen = len(graph)

        for key in graph:
            if not graph[key].IN:   # to remove this
                for key2 in graph[key].OUT:
                    graph[key2].IN.remove(key)
                del graph[key]
                res += key
                break

        if oldlen == len(graph): # if shrinking stops, solution doesn't exist
            return ""
        oldlen = len(graph)
    return res
    
'''

#------------------------------------------------------------------------------

'''

from collections import deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.visited={}
        self.graph={}
        self.results=deque()
        characters=set()
        
        for word in words:
            for char in word:
                self.visited[char]=0
                self.graph[char]=[]
                characters.add(char)
                
        for i in range(len(words)-1):
            word_1=words[i]
            word_2=words[i+1]
            success=self.addEdgeBetweenTwoWords(word_1,word_2)
            if(not success):
                return ""
            
        for char in characters:
            success=self.topologicalSort(char)
            if(not success):
                return ""
            
        return "".join(list(self.results))
            
    def topologicalSort(self,char):
        #detected cycle
        if(self.visited[char]==-1):
            return False
        #char has been visited and completed topological sort on
        if(self.visited[char]==1):
            return True
        
        self.visited[char]=-1
        
        for neighb in self.graph[char]:
            success=self.topologicalSort(neighb)
            if(not success):
                return False
        
        self.visited[char]=1 #mark char as visited and completed topological sort
        
        self.results.appendleft(char)
        
        return True
        
        
        
    
    #an edge between var_1 and var_2 means var_1 precedes var_2
    def _addEdge(self,var_1,var_2):
        self.graph[var_1].append(var_2)
    
    def addEdgeBetweenTwoWords(self,word1,word2):
        for char_1,char_2 in zip(word1,word2):
            if(char_1!=char_2):
                self._addEdge(char_1,char_2)
                return True
        
        #invalid
        #hello world cannot precedes hello. doesn't make sense
        if(len(word1)>len(word2)):
            return False
        return True
        
'''