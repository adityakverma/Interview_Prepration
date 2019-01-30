
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# https://leetcode.com/problems/subsets-ii/discuss/30270/Share-my-5-lines-of-Python-solution
# https://leetcode.com/problems/subsets-ii/discuss/30217/Simple-and-clear-python-solution.
class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, start, cur, res):
        res.append(cur[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            cur.append(nums[i])
            self.backtrack(nums, i+1, cur, res)
            cur.pop()



nums = [1,2,2] # or num = ['A','B','C']
s = Solution()
#print s.subsets(nums)
print "\nSubset without dups :", s.subsetsWithDup(nums)
#print s.subsets_usingSets(nums)

# See this below Awesome
# https://leetcode.com/problems/subsets-ii/discuss/30196/Backtrack-Summary:-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
# https://leetcode.com/problems/subsets-ii/discuss/110976/Simple-backtracking-python-solution-that-solves-both-Subset-and-Subset-II

