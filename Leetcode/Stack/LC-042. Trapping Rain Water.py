
# Tags: Array, Two Pinter, Stack, Google, AWS, Apple, Bloomberg

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it is able to trap after raining.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
# (blue section) are being trapped.



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        