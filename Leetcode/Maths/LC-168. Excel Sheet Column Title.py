

# # Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
#
# Example 1:
#
# Input: 1
# Output: "A"
#
# Example 2:
#
# Input: 28
# Output: "AB"
#
# Example 3:
#
# Input: 701
# Output: "ZY"
# -----------------------------------------------------

class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        # print capitals
        result = []

        while num > 0:
            result.append(
                capitals[(num - 1) % 26])  # We can use (n-1)%26 instead, then we get a number range from 0 to 25.
            # print capitals[(num-1)%26]
            num = (num - 1) // 26  # Floor division.

        result.reverse()
        return ''.join(result)


# https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation

