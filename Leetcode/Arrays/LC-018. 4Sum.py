
# Given an array nums of n integers and an integer target, are there elements a, b, c,
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the
# array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# ====================================================================================

# similar to LC-15. 3Sum

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        answer = []
        length = len(nums)
        for i in range(length - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                start = j + 1
                end = len(nums) - 1
                a = nums[i]
                b = nums[j]
                while (start < end):
                    c = nums[start]
                    d = nums[end]
                    sum = a + b + c + d

                    if sum < target:
                        start = start + 1
                    elif sum > target:
                        end = end - 1
                    else:
                        answer.append([a, b, c, d])
                        # start = start + 1
                        end = end - 1

                        while start < end and nums[start] == nums[start - 1]:
                            start = start + 1
                        while start < end and nums[end] == nums[end + 1]:
                            end = end - 1

        return answer

