
# Tags: Array, Two Pointers, FB, MS

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:

    # ACCEPTED : In place with O(1) extra memory only. But ONLY works for sorted arrays
    def removeDuplicates_LC026(self, nums):
        pos = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                nums[pos] = nums[i]
                pos += 1
        return pos

    # ACCEPTED too. But ONLY works for sorted arrays
    def removeDuplicates_1(self, nums):
        nums[:] = sorted(list(set(nums)))
        return len(nums)


    # Not happy on LC [ My solution] - Length is same, so it works, but real valuses with array are not good
    # Also note, lenght is returned fine, which is what needed, and works for both Sorted and Unsorted array
    def removeDups_UnsortedArray_usingHash(self,arr): # This works for both sorted n unsorted
        my_dict = {}
        for i in arr:
            if my_dict.get(i) == 1: # Duplicate
                pass
            my_dict[i]=1
        return len(my_dict.keys())


if __name__ == '__main__':
    nums_sorted   = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 9, 9, 9, 9, 9]
    nums_unsorted = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 9, 9, 3, 1, 1]
    s = Solution()
    #print s.removeDuplicates(nums)
    print "\nSorted Array ( Accepted  ) : ", s.removeDuplicates_LC026(nums_sorted)

    #---------------------------------------------------------------------------------
    # Not happy on LC - Given input as  [1, 1, 2] Lenght is same but values of arr is [1,1] instead of [1,2]
    #print "\nSorted Array  (Hash table) : ", s.removeDups_UnsortedArray_usingHash(nums_sorted)
    #print "\nUnsorted Array(Hash table) : ", s.removeDups_UnsortedArray_usingHash(nums_unsorted)

