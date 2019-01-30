
# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000
#
# Example 2:
# Input: 2.10000, 3
# Output: 9.26100
# =======================================================================


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #return x**n # Accepted
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


    def myPow_R(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x**n # Accepted

        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n / 2)

