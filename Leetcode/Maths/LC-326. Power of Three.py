
# Given an integer, write a function to determine if it is a power of three.

# Example 1:
# Input: 27
# Output: true
#
# Example 2:
# Input: 0
# Output: false
#
# Example 3:
# Input: 9
# Output: true
#
# Example 4:
# Input: 45
# Output: false

# ============================================================================

import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return True if n == 1 else False

    # ------------------------------------------------------------------
    # READ below two links to understand log solution
    # https://leetcode.com/problems/power-of-three/discuss/77890/simple-python-code
    # https://www.rapidtables.com/math/algebra/Logarithm.html

    def isPowerOfThree_(self, n):

        if n <= 0:
            return False

        temp = math.log10(n) / math.log10(3)
        if temp.is_integer():
            return True
        return False

    # Concept: 3^x = n. Now if x is integer for given n then return True, else False.
    # Note: 3^x = n is log base3 (n) which is log10(n) / log10(3)






