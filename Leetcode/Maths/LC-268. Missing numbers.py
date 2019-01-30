

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

# Example 1:
#
# Input: [3,0,1]
# Output: 2
#
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# =======================================================================

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # return (n*(n+1))/2 - sum(nums) # ACCEPTED - Solution-1. # Sum of natural numbers minus the sum of given numbers

        return sum(range(len(nums) + 1)) - sum(nums)  # ACCEPTED - Solution-2

        # return sum(range(min(nums), (min(nums)+len(nums)+1))) - sum(nums)     # Works perfect if sequence is [4,5,6,8]



