
# Given an unsorted array nums, reorder it in-place such that
# nums[0] <= nums[1] >= nums[2] <= nums[3]....

# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
# ============================================================================


# Approach #1 (Sorting) [Accepted]

# The obvious solution is to just sort the array first, then swap elements pair-wise starting from the second element. For example:
#
#    [1, 2, 3, 4, 5, 6]
#        ↑  ↑  ↑  ↑
#        swap  swap
#
# => [1, 3, 2, 5, 4, 6]

# Solution 1: Sorting:     Just sort the array and swap adjacent elements

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Sorting: Just sort the array and swap adjacent elements
        nums.sort()
        i = 1
        while i+1 < len(nums):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
        return


# Solution 2: O(N) solution in one pass

class Solution_(object):

    def wiggleSort(self, nums):

        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]