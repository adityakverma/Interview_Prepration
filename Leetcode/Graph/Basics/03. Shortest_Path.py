
# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
# Python program to generate shortest path

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function for adding edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to find the shortest path
    def find_shortest_path(self, start, end, path):

        path.append(start)

        if start == end:  # This is only new stuff here for finding shortest path. Rest all is DFS ?
            return path

        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

if __name__ == '__main__':

    # graph = {
    #     'a': ['c'],
    #     'b': ['d'],
    #     'c': ['e'],
    #     'd': ['a', 'd'],
    #     'e': ['b', 'c']
    # }

    # OR declare like this.
    g = Graph()
    g.addEdge('a', 'c')
    g.addEdge('b', 'd')
    g.addEdge('c', 'e')
    g.addEdge('d', 'a')
    g.addEdge('d', 'd')
    g.addEdge('e', 'b')
    g.addEdge('e', 'c')

    print "\nShortest Path is ",g.find_shortest_path('d', 'c', path=[])


# --------------------------------------

'''
graph = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'd'],
    'e': ['b', 'c']
}

# function to find the shortest path
def find_shortest_path(graph, start, end, path):

    path.append(start)

    if start == end:  # This is only new stuff here for finding shortest path. Rest all is DFS ?
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

# Driver function call to print
# the shortest path
print "\nShortest path: ",find_shortest_path(graph, 'd', 'c', path=[])

'''

