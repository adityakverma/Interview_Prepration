
# Tags: Array, Two Pointers, FB
# ==============================

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

class Solution(): # Array Transformation

    # in-place
    def moveZeros1(self, nums):

        self.zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[self.zero] = nums[i]
                self.zero += 1

        while self.zero < len(nums):
            nums[self.zero] = 0
            self.zero += 1

        return nums

    # in-place
    def moveZeros2(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            #print i, zero, nums
        return nums


    # Below looks good and easy, but guess interviewer wants to see array skills without in-build functions.
    def moveZeros3(self, nums):
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

if __name__ == '__main__':

    nums = [1,2,0,0,3,12]
    s = Solution()
    print s.moveZeros1(nums)

    print s.moveZeros2(nums)
    print s.moveZeros3(nums)
