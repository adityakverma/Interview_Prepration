
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination
# should be a unique set of numbers.
#
# Note:
#
#     All numbers will be positive integers.
#     The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# -------------------------------------------------------------------------

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if n > sum([i for i in range(1,
                                     11)]):  # Corner case, where n = 1000 and sum from 1-9 can never fulfil that number, so return [].
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res

    def sum_help(self, k, n, start, cur, res):
        if len(cur) == k:
            if sum(cur) == n:
                res.append(list(cur))
            return

        if len(cur) > k or start > 9:  # again corner case where size of cur > k OR start > 9 [start needs within 9]
            return

        for i in range(start, 10):  # start is updated - Just like LC-077
            cur.append(i)
            self.sum_help(k, n, i + 1, cur, res)
            cur.pop()

    # Note: There is another way to doing these combination sum problems - where we keep adding path sum. See below.
    # https://leetcode.com/problems/combination-sum-iii/discuss/60805/Easy-to-understand-Python-solution-(backtracking).
    '''    
    def combinationSum3(self, k, n):       
        res = []
        self.dfs(xrange(1,10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)  
     '''


