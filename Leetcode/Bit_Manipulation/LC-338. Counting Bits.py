
# Given a non negative integer number num. For every numbers i in the range
# 0 ≤ i ≤ num calculate the number of 1's in their binary representation
# and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]

#====================================================

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        res = [0]
        for i in xrange(1, num + 1):
            res.append(res[i >> 1] + (i & 1))
        return res

# The number of 1's in the binary representation of 0 is clearly 0 (base case). For a number n, the number of 1's in its binary representation will be determined as follows:

# If n is odd, the last digit is a '1', so a right shift (which is the same as n//2) will eliminate one 1.
# If n is even, the last digit is a '0', so a right shift (i.e. n//2) will have the same number of 1's

# Aditya: To find number of one in 9, we see how many number of one in res[n//2] which is res[4] which will be 1 + last bit ( whatever it is), which will be 1 so (i&1) = 1, so total ones in number 9 is two so answer is 2. Similarly we find for all other numbers ... [1..n]


