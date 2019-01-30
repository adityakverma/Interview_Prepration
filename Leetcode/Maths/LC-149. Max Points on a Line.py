
# Given n points on a 2D plane, find the maximum number of points that lie on the
# same straight line.
#
# Example 1:
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4

# ------------------------------------------------------------------------------------

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

"""
First, let's talk about mathematics.
How to determine if three points are on the same line?
The answer is to see if slopes of arbitrary two pairs are the same.

Second, let's see what the minimum time complexity can be.
Definitely, O(n^2). It's because you have to calculate all slopes between any two points.

Then let's go back to the solution of this problem.
In order to make this discussion simpler, let's pick a random point A as an example.
Given point A, we need to calculate all slopes between A and other points. There will be three cases:
Some other point is the same as point A.
Some other point has the same x coordinate as point A, which will result to a positive infinite slope.

General case. We can calculate slope. We can store all slopes in a hash table.
And we find which slope shows up mostly. Then add the number of same points to it (overlap).
Then we know the maximum number of points on the same line for point A.

Similarly, We can do the same thing to point B, point C...
Finally, just return the maximum result among point A, point B, point C..."""


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import sys
        n = len(points)
        if n <= 2:
            return n
        maxpoints = 0
        for i in range(n):
            overlap = 1
            slopdict = {}
            for j in range(i + 1, n):
                x = points[i].x - points[j].x
                y = points[i].y - points[j].y
                if x == 0 and y == 0:
                    overlap += 1
                    continue

                # find the slope
                if x == 0:
                    slope = sys.maxint  # point has the same x coordinate as point A, which will result to a positive infinite slope.
                else:
                    slope = float(y) / float(x)

                # Add slope in Hashtable
                if slope not in slopdict:
                    slopdict[slope] = 1
                else:
                    slopdict[slope] = slopdict[slope] + 1  # Same  slope means both points are in same line.

            maxlocal = 0
            for val in slopdict.values():
                maxlocal = max(val, maxlocal)
            maxlocal += overlap
            maxpoints = max(maxlocal,
                            maxpoints)  # Max no. of points for specific slope slopdict.values()- means max no of points onthat slope

        return maxpoints


# this is accepted solution before, but now they added few NEW test cases so this doesn't submit.

