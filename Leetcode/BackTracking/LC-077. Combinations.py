
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# -------------------------------------------------------------------------
import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(n, k, 1, [], res)
        return res

    def backtrack(self, n, k, start, cur, res):

        if k == len(cur):
            res.append(copy.deepcopy(cur))  # Deep copy, else its all empty
            return

        for i in range(start,
                       n + 1):  # Note here we are not starting from 1 everytime, instead we are using 'start', which is actually i+1
            cur.append(i)
            self.backtrack(n, k, i + 1, cur, res)
            cur.pop()

        # https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

####################################################################################################

'''

My original Solution

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(n,k,1,[],res)
        return res
    
    def backtrack(self, n, k, start, cur, res):
        if k == len(cur):
            print cur
            #res.append(cur)
            return
            
        for i in range(1,n+1,1):  # Here I am starting from 1 everytime, but working solution starts from 'start' which is actually i+1 during call.
            cur.append(i)
            self.backtrack(n,k,i+1, cur, res)
            cur.pop()

------

Other's Working Solution. Only subtle difference. ( which is start variable in for loop)

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        
        def DFS(results, cur, start, n, k):
            if(k==len(cur)):
                results.append(copy.deepcopy(cur))	# python append()
                return  
            for i in range(start,n+1,1):
                cur.append(i)
                DFS(results, cur, i+1, n, k)
                cur.pop()
        
        DFS(results, cur, 1, n, k)
        return results
'''