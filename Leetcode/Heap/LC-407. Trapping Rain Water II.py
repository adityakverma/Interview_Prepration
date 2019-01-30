
# LC-42 - Trapping Rain Water - I

# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# Note:
#
# Both m and n are less than 110. The height of each unit cell is greater than
#  0 and is less than 20,000.

# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.
# https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
# https://leetcode.com/problems/trapping-rain-water-ii/discuss/185437/python3-BFS-+-Heap-1D-case-and-2D-case

# --------------------------------------------------------------------------------

# Best Solution Video: https://www.youtube.com/watch?time_continue=53&v=cJayBq38VYw

# Let the water flow from boundaries. We don't care so we will make minHeap from 4 borders
# which we can use to find water collected for inner cells of matrix.
# So once we have Minheap of all four border line. Then we pop min from heap and visit its
# neighbour. Now if height of neighbour is less then height of popped element then water
# will be trapped. Find that water.

# Concept used -  Heap, DFS

class Solution(object):

    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        import heapq
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in xrange(m)]

        # Push all the block on the border into heap
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result

if __name__ == '__main__':

    height = [[1,4,3,1,3,2],
              [3,2,1,3,2,4],
              [2,3,3,2,3,1]]

    s = Solution()
    print "\nTotal water Trapped: ",s.trapRainWater(height)

##################################################################


'''

# Balaji

class Solution(object):

    import heapq
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False]  * n for _ in range(m)]

        heaplist = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heaplist,(heightMap[i][j], i, j))
                    visited[i][j] = True

        maxwater = 0

        while(heaplist):
            height, i, j = heapq.heappop(heaplist)
            for x,y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x <= 0 or x >= m or y <=0 or y >= n:
                    continue
                if not visited[x][y]:
                    maxwater += max(0, height - heightMap[x][y])
                    heapq.heappush(heaplist, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = True

        return maxwater


'''