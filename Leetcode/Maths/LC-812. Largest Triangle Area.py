

# You have a list of points in the plane. Return the area of the largest triangle
# that can be formed by any 3 of the points.

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.

# ---------------------------------------------------------------------------------------

class Solution(object):

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # Idea: For each possible triangle, check it's area and keep the area of the largest.
        # Algorithm: We will have 3 for loops to cycle through each choice of 3 points in the array.
        # After, we'll need a function to calculate the area given 3 points. Here we have some options:
        # We can use the Shoelace formula directly, which tells us the area given the 3 points;


        N = len(points)
        ma = 0
        def calArea(x1, y1, x2, y2, x3, y3):
            return abs( 0.5 *( x1 *( y2 -y3 ) + x2 *( y3 -y1 ) + x3 *( y1 -y2)))


        for i in range( N -2):
            for j in range( i +1, N- 1):
                for k in range(j + 1, N):
                    ma = max(ma, calArea(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0],points[k][1]))
        return ma

