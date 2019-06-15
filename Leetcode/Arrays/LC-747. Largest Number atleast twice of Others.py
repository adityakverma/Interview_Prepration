
# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.
#
# Example 1:
#
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
#
#
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


class Solution():
    # My Solution. LC Accepted in first attempt.
    def largestNumAtleastTwice_LC747(self, nums):
        largest = max(nums)
        for i in range(len(nums)):
            if largest < 2 * nums[i] and nums[i] != largest:
                return -1
        return nums.index(largest)

    def dominantIndex(self, nums):
        k = max(nums)
        x = nums.index(k)
        for i in range(len(nums)):
            if i == x:
                continue
            else:
                if nums[i] * 2 > k:
                    return -1
        return x

if __name__ == '__main__':
    s = Solution()
    arr = [3, 6, 1, 0]
    print "\nLargest number atleast twice of others is at index at:", s.largestNumAtleastTwice_LC747(arr)