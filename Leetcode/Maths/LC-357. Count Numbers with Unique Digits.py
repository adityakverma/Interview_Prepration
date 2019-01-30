#
# # Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
#              excluding 11,22,33,44,55,66,77,88,99
# ========================================================================================
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans


# For the first (most left) digit, we have 9 options (no zero); for the second digit we used one but we can use 0 now, so 9 options; and we have 1 less option for each following digits. Number can not be longer than 10 digits.

# The variable tmp at iteration i denotes the number of i-digit integers with unique digits. It's easy to see that tmp = 9 when i = 1 (excluding 0), tmp = 9 * 9 when i = 2, tmp = 9 * 9 * 8 when i = 3, ..., tmp = 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 when i = 10. When i > 10, every integer with i digits must have duplicated digits. The solution res can be constructed iteratively by adding up the tmp from each iteration. Finally we return res + 1 to include 0.
