
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# ======================================================================

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if a == -b:
            return 0

        if abs(a) > abs(b):  # Example a = -11, b=2 will give TLE if this if is removed.
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)

        while b:
            c = a & b
            a ^= b
            b = c << 1

        return a

    # Algorithm:
    # =========
    # Step-1: Do & of a and b which gives carry we need
    # Step-2: We do XOR operation, which can help in getting actual addition
    # Step-3: Then we left shift all carry, so we can apply to XOR'd result.

    # https://www.youtube.com/watch?v=qq64FrA2UXQ
