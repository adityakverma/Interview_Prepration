
# Approach Idea # 1
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be
# impossible to take all courses.

# Thus, we need to come up with a DFS algorithm to detect a cycle in the directed graph.
# Here I used HashSet and recursion stack to detect cycle. For example, if we have two
# vertices connected with each other(1->0, 0->1). if we start DFS with vertex 1, add
# vertex 1 into HashSet. Then we explore further finding vertex 0 is the neighbor of vertex 1.
# Then add vertex 0 into HashSet. Keep exploring the neighbor of vertex 0 until we realized
# that we already have 1 in HashSet. Cycle Detected!

# https://leetcode.com/problems/course-schedule/discuss/58731/Share-my-Java-solution-with-detail-comment

# https://leetcode.com/problems/course-schedule/discuss/58514/Three-python-solutions:-BFS-DFS-recursively-DFS-iteratively
# https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
# https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-+-E)-time-and-O(V-+-E)-space

from collections import defaultdict

class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # edge case
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
        seen, in_stack = set(), set()

        def circle(seen, in_stack, v):
            seen.add(v)
            in_stack.add(v)
            for neighbor in graph[v]:
                if neighbor not in seen:
                    if circle(seen, in_stack, neighbor):
                        return True
                else:
                    if neighbor in in_stack:
                        return True
            in_stack.discard(v)
            return False

        for i, j in prerequisites:
            if j not in seen:
                if circle(seen, in_stack, j):
                    return False
        return len(seen) <= numCourses



if __name__ == '__main__':

    numCourses = 2
    prerequisites = [[1,0],[0,1]]

    s = Solution()
    print s.canFinish(numCourses,prerequisites)



