
# https://docs.python.org/3/library/collections.html#collections.defaultdict
# defaultdict 	dict subclass that calls a factory function to supply missing values
# Counter 	dict subclass for counting hashable objects

# Aditya: So we have two Dict and one list.
# defaultdict ( container datatype) from collection - for graph representation
# Counter ( container datatype) from collection - for distance-map
# list ( default datatype) - for making queue of vertex

from collections import Counter
from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)   # Container datatypes 1

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS_aditya(self, source):

        queue = []
        queue.append(source)

        dist = defaultdict(list)
        dist[source] = 0            # Map

        while queue:
            node = queue.pop(0)
            print node,

            for neighbour in self.graph[node]:
                if neighbour not in dist:
                    dist[neighbour] = dist[node] +1
                    queue.append(neighbour)

        print "\nDistance map is ",(dist.items()) # Additional Info

# Driver code
# Create a graph given in the above diagram
if __name__ == '__main__':
    g1 = Graph()
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(2, 0)
    g1.addEdge(2, 3)
    g1.addEdge(3, 3)
    g1.addEdge(1, 4)


    g2 = Graph()
    g2.addEdge('a', 'c')
    g2.addEdge('b', 'd')
    g2.addEdge('c', 'e')
    g2.addEdge('d', 'a')
    g2.addEdge('d', 'd')
    g2.addEdge('e', 'b')
    g2.addEdge('e', 'c')

    # graph = {
    #     'a': ['c'],
    #     'b': ['d'],
    #     'c': ['e'],
    #     'd': ['a', 'd'],
    #     'e': ['b', 'c']
    # }

    print "\n\nFollowing is BFS (starting from vertex 2) is ",
    g1.BFS_aditya(2)

    print "\n\nFollowing is BFS (starting from vertex d) is ",
    g2.BFS_aditya('d')

    print "\n\nNOTE: this is correct, because this is Directed graph"

#################################################################

# collections - Container datatypes

#
# This module implements specialized container datatypes providing alternatives to Pythons
# general purpose built-in containers, dict, list, set, and tuple.

# namedtuple() 	factory function for creating tuple subclasses with named fields
#### deque 	Double-ended Queue. list-like container with fast appends and pops on either end
# ChainMap 	dict-like class for creating a single view of multiple mappings
#### Counter 	dict subclass for counting hashable objects
# OrderedDict 	dict subclass that remembers the order entries were added
#### defaultdict 	dict subclass that calls a factory function to supply missing values
# UserDict 	wrapper around dictionary objects for easier dict subclassing
# UserList 	wrapper around list objects for easier list subclassing
# UserString 	wrapper around string objects for easier string subclassing

