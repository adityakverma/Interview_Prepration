

# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
#
#
#
# Example 1:
#
# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# =====================================================================

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while n:
            n = n & (n - 1)  # This reduces '1' from rightmost eveytime & then we increment count. It does cut the last digit 1 in the binary.
            count += 1
        return count