
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus,
# the itinerary must begin with JFK.

# Note:
#
#     If there are multiple valid itineraries, you should return the itinerary that has the smallest
# lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller
# lexical order than ["JFK", "LGB"].

#     All airports are represented by three capital letters (IATA code).
#     You may assume all tickets form at least one valid itinerary.

# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.


# The nice thing about DFS is it tries a path, and if that's wrong (i.e. path does not lead to solution), DFS goes one step back and tries another path. It continues to do so until we've found the correct path (which leads to the solution). You need to always bear this nice feature in mind when utilizing DFS to solve problems.

#----------------------------------------------------------------------------------

# In this problem, the path we are going to find is an itinerary which:
#
#     uses all tickets to travel among airports
#     preferably in ascending lexical order of airport code
#
# Keep in mind that requirement 1 must be satisfied before we consider 2. If we always choose the airport with the smallest lexical order, this would lead to a perfectly lexical-ordered itinerary, but pay attention that when doing so, there can be a "dead end" somewhere in the tickets such that we are not able visit all airports (or we can't use all our tickets), which is bad because it fails to satisfy requirement 1 of this problem. Thus we need to take a step back and try other possible airports, which might not give us a perfectly ordered solution, but will use all tickets and cover all airports.
#
# Thus it's natural to think about the "backtracking" feature of DFS. We start by building a graph and then sorting vertices in the adjacency list so that when we traverse the graph later, we can guarantee the lexical order of the itinerary can be as good as possible. When we have generated an itinerary, we check if we have used all our airline tickets. If not, we revert the change and try another ticket. We keep trying until we have used all our tickets.

#-----------------------------------------------------------------------------------------
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78772/Python-Dfs-Backtracking

#Python Dfs Backtracking

#I use a dictionary to represent the tickets (start -> [list of possible destinations]). Then, I start the route at JFK and I dfs from there. Since I do the dfs in sorted order, the first time that I find a possible route, I can return it and know that it is in the smallest lexigraphic order. Finally, note that the worked variable either contains None (as a result of a failed search) or the correct route.

import collections

def findItinerary(self, tickets):
    d = collections.defaultdict(list)
    
    for flight in tickets:
        d[flight[0]] += flight[1],
    self.route = ["JFK"]
    def dfs(start = 'JFK'):
        if len(self.route) == len(tickets) + 1:
            return self.route
        myDsts = sorted(d[start])
        for dst in myDsts:
            d[start].remove(dst)
            self.route += dst,
            worked = dfs(dst)
            if worked:
                return worked
            self.route.pop()
            d[start] += dst,
    return dfs()

#####################################################

# A variant of DFS.
# When traversing, move the smallest neighbour that you are
# going to visit to the worst position in its neighbour list.

# https://leetcode.com/problems/reconstruct-itinerary/discuss/78825/Clear-Python-DFS

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import deque
        graph = {}
        for ticket in tickets:
            graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]
        for start in graph:
            graph[start] = deque(sorted(graph[start]))

        def dfs(root, graph, path, maxLen):
            if len(path) == maxLen:
                return True
            for k in xrange(len(graph.get(root, []))):
                end = graph[root].popleft()
                path.append(end)
                if dfs(end, graph, path, maxLen):
                    return True
                path.pop()
                graph[root].append(end)

        path = ["JFK"]
        dfs("JFK", graph, path, len(tickets) + 1)
        return path

###################################################################

# https://leetcode.com/problems/reconstruct-itinerary/discuss/78827/Solve-both-recursively-and-iteratively-in-Python

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = self.buildGraph(tickets)
        path = []
        path.append("JFK")
        self.dfs(graph, path, tickets)
        return path

    def dfs(self, graph, path, tickets):
        to = graph[path[-1]]
        to.sort()
        for i in range(len(to)):
            d = to.pop(i)
            path.append(d)
            self.dfs(graph, path, tickets)
            if len(path) == len(tickets) + 1:
                return
            path.pop()
            to.insert(i, d)
        return

    def buildGraph(self, tickets):
        graph = dict()
        for ticket in tickets:
            if ticket[0] in graph:
                graph[ticket[0]].append(ticket[1])
            else:
                graph[ticket[0]] = [ticket[1]]
            if ticket[1] not in graph:
                graph[ticket[1]] = []
        return graph


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = self.buildGraph(tickets)
        path = []
        path.append("JFK")
        self.dfs(graph, path, tickets)
        return path

    def dfs(self, graph, path, tickets):
        dq = graph[path[-1]]
        count = len(dq)
        while count > 0:
            count -= 1
            path.append(dq.popleft())
            self.dfs(graph, path, tickets)
            if len(path) == len(tickets) + 1:
                return
            dq.append(path.pop())
        return

    def buildGraph(self, tickets):
        graph = dict()
        for ticket in tickets:
            if ticket[0] in graph:
                graph[ticket[0]].append(ticket[1])
            else:
                graph[ticket[0]] = [ticket[1]]
            if ticket[1] not in graph:
                graph[ticket[1]] = []
        for d in graph:
            temp = graph[d]
            temp.sort()
            graph[d] = collections.deque(temp)
        return graph


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = self.buildDigraph(tickets)
        result = []
        stack = ["JFK"]
        while len(stack) != 0:
            u = stack[-1]
            adj = graph[u]
            adj.sort()
            adj.reverse()
            if len(adj) == 0:
                result.append(stack.pop())
            else:
                stack.append(adj.pop())
        result.reverse()
        return result

    def buildDigraph(self, arcs):
        graph = {}
        for arc in arcs:
            if arc[0] in graph:
                graph[arc[0]].append(arc[1])
            else:
                graph[arc[0]] = [arc[1]]
            if arc[1] not in graph:
                graph[arc[1]] = []
        return graph


############################################################################




