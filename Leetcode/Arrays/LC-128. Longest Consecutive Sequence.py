
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# ------------------------------------------------------------------------------------------------


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num=set(nums) # First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.
        maxLen=0

        while num:

            l1=0
            l2=0
            n=num.pop( )

            i=n+1
            while i in num:
                num.remove(i)
                i+=1  # Add one to current number and find it exists in set. If yes, increment variable l1
                l1+=1

            i=n-1
            while i in num:
                num.remove(i)
                i-=1  # Now subtract one to current number and find it exists in set. If yes, increment variable l2
                l2+=1

            maxLen=max( maxLen,l1+l2+1)
        return maxLen

