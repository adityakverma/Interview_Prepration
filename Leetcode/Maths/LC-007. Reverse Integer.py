
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
# ================================================================

class Solution(object):

    def reverse(self, x):

        negFlag = 1

        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1]) # Get Reverse

        return 0 if x > pow(2, 31) else x * negFlag # (n < 2^31) makes sure x is in range of uint32
