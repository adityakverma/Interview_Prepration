
# 231. Power of Two
# Given an integer, write a function to determine if it is a power of two.

# Example 1:
#
# Input: 1
# Output: true
# Explanation: 20 = 1
#
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 24 = 16
# =========================================================================

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n&(n-1) == 0


# Property : n & (n-1) will be zero only if n is power of 2