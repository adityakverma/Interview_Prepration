
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.

# # Example 1:
# Given nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

# Example 2:
# Given nums = [0,0,1,1,1,1,2,3,3],
# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

class Solution():
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/28128/Python-9-lines-2-extra-variables-76ms.-Any-simpler-solution-else

    # Accepted. But ONLY works for Sorted arrays ( as given).
    def removeDuplicatesII_LC080(self, nums):
        if len(nums) < 3:
            return len(nums)
        pos = 1
        for i in range(1, len(nums)-1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1

    # Just for reference here - LC-026
    def removeDuplicates_LC026(self, nums):
        pos = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                nums[pos] = nums[i]
                pos += 1
        return pos

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return nums
        for i in list(set(nums)):
            if nums.count(i)>2:
                while nums.count(i)!=2:
                    nums.remove(i)
        return len(nums)


def main():
    nums_sorted   = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 9, 9, 9, 9, 9]
    nums_unsorted = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 9, 9, 3, 1, 1]
    s = Solution()
    print "\nSorted Array  : ", s.removeDuplicates(nums_sorted)
    print "\nSorted Array  : ", s.removeDuplicatesII_LC080(nums_sorted)

if __name__ == '__main__':
    main()