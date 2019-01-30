#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# ==============================================================================

class Solution(object):
    numSquaresDP = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = []
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v ** 2 for v in xrange(1, int(math.sqrt(n)) + 1)]
            print perfectSqr

            for i in xrange(len(self.numSquaresDP), n + 1):
                for sqr in perfectSqr:
                    if sqr <= i:
                        j = 1 + self.numSquaresDP[i - sqr]
                        s.append(j)
                self.numSquaresDP.append(min(s))
                s = []  # clear the list before finding the min of next number

                # self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr <= i))

        return self.numSquaresDP[n]

