
# Tags: Strings, BFS, Amazon, Backtracking
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest
# transformation sequence(s) from beginWord to endWord, such that:
#
#     Only one letter can be changed at a time
#     Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
# Note:
#     Return an empty list if there is no such transformation sequence.
#     All words have the same length.
#     All words contain only lowercase alphabetic characters.
#     You may assume no duplicates in the word list.
#     You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#
# Example 2:
# Input:  beginWord = "hit", endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Graphs/Word%20Ladder%20Example%20Problem.ipynb
# https://www.youtube.com/watch?v=AllD5Hiq5VE

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)   # Container datatypes 1

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS_aditya(self, source, target):

        queue = []
        queue.append(source)

        dist = defaultdict(list)
        dist[source] = 0

        while queue:
            node = queue.pop(0)
            print node,

            for neighbour in self.graph[node]:
                if neighbour not in dist.keys():
                    dist[neighbour] = dist[node] +1
                    queue.append(neighbour)
                    #if target == dist[neighbour]:
                    #    break
        #print "\nDistance map is ",\
        #    (dist.items())

if __name__ == '__main__':
    d = {}
    g = Graph()

    source = "hit"
    target = "cog"
    #wordList = ["hit","lot", "log", "cog", "hot", "dot", "dog"]
    wordList = ["hit","lot", "log", "cog", "hot"]

    # create buckets of words that differ by one letter
    for word in wordList:
        #print word
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            #print "bucket",bucket
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    #print "\nPrinting buckets :",d.items()
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    # Now do BFS, to find the path from start to end.
    print "\nWord Ladder is:",g.BFS_aditya(source, target)