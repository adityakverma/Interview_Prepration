


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        res = [1] * (n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                _max = max(j * res[i-j], j * (i-j))
                res[i] = max(res[i], _max)
        return res[n]

