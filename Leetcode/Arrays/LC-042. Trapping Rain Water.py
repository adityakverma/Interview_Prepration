
# Tags: Array, Two Pointer, Stack, Google, AWS, Apple
# ===================================================

# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# ------------------------------------------------------------------------------------

class Solution(object):  # Submitted on 3/26/2019

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # The water we trapped depends on the left side and right side which has the max height,

        if not height or len(height) < 3:
            return 0

        water = 0
        LMax = [0] * len(height)
        RMax = [0] * len(height)

        LMax[0] = height[0]
        for i in range(1, len(height)):  # Note in range last one is not considered. Also last one will not hold any water for sure.
            LMax[i] = max(height[i], LMax[i - 1])  # Max from left to right

        RMax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            RMax[i] = max(height[i], RMax[i + 1])  # Max from right to left

        # print LMax, RMax

        for i in range(len(height) - 1):
            water += min(LMax[i], RMax[i]) - height[i]

        return water


        # https://leetcode.com/problems/trapping-rain-water/solution/?page=5

        # Algorithm
        # =========
        # Find maximum height of bar from the left end upto an index i in the array left_max
        # Find maximum height of bar from the right end upto an index i in the array right_max
        # Iterate over the height array and update ans:
        #   Add min(max_left[i],max_right[i])−height[i] to ans































###########################################################################################
# https://leetcode.com/problems/trapping-rain-water-ii/discuss/185437/python3-BFS-+-Heap-1D-case-and-2D-case

from heapq import *

class element(object):
    def __init__(self, index, height):
        self.index = index
        self.height = height

    def __lt__(self, other):
        return self.height < other.height

class Solution:

    def trapRainWater(self, height):
        L = len(height)
        if L <= 2: return 0

        heap, visited = [], set()

        # Push corner edges into heap ( as we allow water to spill from corner).
        # Also this will for base to calculate water trapped.
        for i in 0, L - 1:
            heap.append(element(i, height[i]))
            visited.add(i)
        heapify(heap)
        max_visited, water = 0, 0

        while heap:
            node = heappop(heap)
            i, h = node.index, node.height
            if h > max_visited:
                max_visited = h
            else:
                water += max_visited - h
            for ni in i - 1, i + 1:
                if 0 <= ni < L and ni not in visited:
                    heappush(heap, element(ni, height[ni]))
                    visited.add(ni)
        return water

if __name__ == '__main__':

    h = [0,1,0,2,1,0,1,3,2,1,2,1]

    s = Solution()
    print "\nTotal water Trapped-I :",s.trapRainWater(h)



'''

Python solutions, O(n) space and O(1) space

The water we trapped depends on the left side and right side which has the max height,

We keep the left side and right side until we find a higher side

class Solution:
# @param A, a list of integers
# @return an integer
def trap(self, arr):
    height, left, right, water = [], 0, 0, 0
    for i in arr:
        left = max(left, i)
        height.append(left)
    height.reverse()
    for n, i in enumerate(reversed(arr)):
        right = max(right, i)
        water += min(height[n], right) - i
    return water

'''

####################################################################
# 3/25/19:

# https://www.youtube.com/watch?v=HmBbcDiJapY

def trap(self, heights):
    if not height or len(height) < 3:
        return 0

    water = 0
    LMax = [0] * len(heights)
    RMax = [0] * len(heights)

    LMax[0] = heights[0]
    for i in range(len(heights)):
        LMax[i] = max(heights[i], LMax[i - 1])

    RMax[len(heights) - 1] = heights[len(heights) - 1]
    for i in range(len(heights) - 2, 0, -1):
        RMax[i] = max(heights[i], RMax[i + 1])

    for i in range(len(heights) - 1):
        water += min(LMax[i], RMax[i]) - heights[i]

    return water

# #2 is not DP actually, because the problem is not divided into 2 sub-problems, but 2 partial problems. It's just memoization. Although memoization is often used with DP, they're different concepts. Don't be misleading.
