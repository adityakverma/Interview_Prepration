
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

##############################################################################

class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # swap such that a will be large
        if len(a) < len(b):
            a, b = b, a

        ans = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while( j >= 0):
            sum = int(a[i]) + int(b[j]) + carry
            ans = str(sum % 2) + ans
            carry = sum/2
            i = i - 1
            j = j - 1

        while( i >= 0) :
            sum = int(a[i]) + carry
            ans = str(sum % 2) + ans
            carry = sum / 2
            i = i - 1

        if carry == 1:
            ans = "1" + ans
        return ans


# Also check LC-002. Similar Concept