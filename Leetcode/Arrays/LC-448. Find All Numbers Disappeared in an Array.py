
# Given an array of integers, some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
# Input: [4,3,2,7,8,2,3,1]
# Output: [5,6]

class Solution():

    # -----------------------------------------------------------

    # Solution using Extra Space :
    # Use a set (hash-map) and add all the numbers in this set. The set consists of all unique values within nums.
    # Iterate from [1 to N] and add to result list if i is not in the marked set.

    def findDisappearedNumbersBetter(self, nums):
        if nums == []: return []

        n = len(nums)
        nums = set(nums)
        output = []
        for i in range(1, n+1):
            if i not in nums:
                output.append(i)
        return output

    # -----------------------------------------------------------
    # Solution without using Extra Space
    # Can we avoid the set and somehow mark the input array which tells us what numbers are seen and what are not? We have additional information that the numbers are positive and numbers lie between 1 and N.
    # Approach 1: Iterate the array and mark the position implied by every element as negative. Then in the second iteration, we simply need to report the positive numbers.

    def findDisappearedNumbers_(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x-1] = -1*abs(nums[x-1])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
    # -----------------------------------------------------------



# difference between set3 and set4
# set5 = set3 - set4