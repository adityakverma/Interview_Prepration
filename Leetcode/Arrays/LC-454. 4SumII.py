#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        def buildDict(L1, L2, dic):
            for val1 in L1:
                for val2 in L2:
                    if (val1 + val2) not in dic:
                        dic[val1 + val2] = 1
                    else:
                        dic[val1 + val2] += 1

        dict1 = {}
        dict2 = {}
        buildDict(A ,B, dict1)
        buildDict(C ,D, dict2)

        count = 0

        for val in dict1:
            if (-1 ) *val in dict2:
                count += dict1[val] * dict2[-val]

        return count

