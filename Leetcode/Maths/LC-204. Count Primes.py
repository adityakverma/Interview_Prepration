
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# -------------------------------------------------------------------------

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [False] * n
        count = 0
        for i in range(2, n):
            if memo[i] == False:
                count += 1

                # And mark all muliple as True, so we avoid check if we see again
                for j in xrange(2, (n - 1) // i + 1):
                    memo[i * j] = True
        return count


#---------------- Balaji below -----------------------------

class Solution_(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        primeFlag = [True] * n
        for i in range(2, n):
            if primeFlag[i]:
                count += 1
                j = 1
                while(i*j < n):
                    primeFlag[i*j] = False
                    j += 1
        return count
    
