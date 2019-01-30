
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
# Example 1:
#
# Input: "A"
# Output: 1
#
# Example 2:
#
# Input: "AB"
# Output: 28
# =================================================================================

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum

# Example : DYC = (4 * 26^2) + (25 * 26^1) + (3 * 25^0)
#               = 2704 + 51 + 3 = 2758