
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
# ---------------------------------------------------------------------------------

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

        # Step-1: Find non-increasing suffix from end - Example "2" if nums = [0,1,2,5,3,3,0]
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:  # If all nums are in descending order - then we simply reverse whole list. Eg: [3,2,1] will give ans = [1,2,3]
            nums.reverse()
            return

            # Step-2: Find the right most successor's position of pivot element "2" in remaining subarray. Example nums = [0,1,2,5,3,3,0] and pivot was 2 so right most successor's position in remaining subarray [5,3,3,0] from end is '3'. Swap those.
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Step-3: Reverse the subarray after swap(from step-2). Meaning [5,3,2,0] becomes [0,2,3,5]
        nums[i:] = nums[len(nums) - 1: i - 1: -1]
        return True

    # Algorithm:
    # See the steps-1,2,3 above





