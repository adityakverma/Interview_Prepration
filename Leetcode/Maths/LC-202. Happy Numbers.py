
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any
# positive integer, replace the number by the sum of the squares of its digits,
#  and repeat the process until the number equals 1 (where it will stay), or it
#  loops endlessly in a cycle which does not include 1. Those numbers for which
#  this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 02 = 1
# ================================================================================

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Hash = {}

        while n != 1:  # Keep checking until n is not 1. Meanwhile if n is present in hash- means its getting in loop so False
            if n in Hash:
                return False
            else:
                Hash[n] = True

            n = sum([pow(int(c), 2) for c in str(n)])

        return True

    

