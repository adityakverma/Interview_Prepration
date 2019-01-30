
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take
# course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of
# courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible
# to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
#
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

# Note:
#     The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
#     Read more about how a graph is represented.
#     You may assume that there are no duplicate edges in the input prerequisites.

# [Aditya]: ############# This is PURE topological Sort. ####################
# Python program to print topological sorting of a DAG

# #  O(V+E) time and O(V+E) space [ Or O(V) space)
from collections import defaultdict

class Graph:  # [This is my Solution. Works Well, but not submitted. But don't worry. Just take it]

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)
        #stack.append(v)

    def topologicalSort(self):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        return stack # when this prints - it prints from top element to bottom ones.

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = numCourses  # No. of vertices

        # edge case
        if not prerequisites:
            return 0

        # Create Graph by adding courses
        for course, prereq in prerequisites:
            self.graph[prereq].append(course)  # Important - See how we are adding. Because way input is provided is [course, prereq]. Otherwise we have to do stack.append(v) instead of  stack.insert(0, v)

        return self.topologicalSort()

if __name__ == '__main__':

    totalCourses = 4
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]

    g = Graph()
    print "\nOrder of taking courses:",g.findOrder(totalCourses, prereqs)


# https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
