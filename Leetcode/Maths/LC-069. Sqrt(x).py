
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
#
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
# ============================================================================================

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        low = 1
        high = x
        mark = 1
        while low != high - 1:

            mid = (high + low) / 2

            if mid > x/ mid:
                high = mid

            elif mid < x/mid:
                mark = mid
                low = mid

            else:
                return mid

        return mark


# We use mid > x/mid instead of mid*mid > x
# rationale behind mid <= x / mid instead of using mid * mid <= x is just for preventing from overflow


# ==================================================

class Solution_(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        low = 1
        high = x
        mark = 1
        while low != high - 1:

            mid = (high + low) / 2
            if mid ** 2 > x:
                high = mid
            elif mid ** 2 < x:
                mark = mid
                low = mid
            else:
                return mid
        return mark


