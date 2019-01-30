
# Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

# Note:
#
#     input and output values are in floating-point.
#     radius and x-y position of the center of the circle is passed into the class constructor.
#     a point on the circumference of the circle is considered to be in the circle.
#     randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
#
# Example 1:
#
# Input:
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
#
# Example 2:
#
# Input:
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# ===============================================================================

import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        x = y = self.radius
        while x ** 2 + y ** 2 > self.radius ** 2:  # Keep finding x and y until its not inside the given circle which has radius r.
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
        # print "X", self.x, x
        # print "Y", self.y, y
        return [self.x + x, self.y + y]

# ================================================================================

# Seems it checks distribution. I tried to return only points in 1/2 of radius and got wrong answer.
# BTW, I want to note, checking distribution it a bit weird, given that task do not specify what kind of distribution should be.
# For example, lets compare two solutions:
# A. make random double in range (x - r, x + r) and (y - r, y + r). check if (x – a)^2 + (y – b)^2 < R^2, if true return, if else repeat
# B. make random double in range (0 - 360) and another one in (0, r). calculate sin/cos to find vector and multiple on radius.
#
# They will give very different but random distribution.

# ================================================================================
# https://www.tutorialspoint.com/python/number_uniform.htm
# Random function generates the random varible between given upper and lower limit.
# print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)
# print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)

# Random Float uniform(5, 10) :  5.52615217015
# Random Float uniform(7, 14) :  12.5326369199
# ================================================================================
