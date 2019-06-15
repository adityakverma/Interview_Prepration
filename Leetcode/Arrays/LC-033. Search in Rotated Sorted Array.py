
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/128702/Clear-Python-binary-search-Solution-with-explanation


class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2 # mid = (low + high) / 2 can get you integer overflow, I prefer mid = low + (high-low)/2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    # -----------------------------------------------

    def search1(self, nums, target):  # Doesn't look good, but answer is ok
        if target in nums:
            return nums.index(target)
        return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1

    s = Solution()
    print s.search(nums,target)
    print s.search1(nums, target)



# So the idea is that this method uses l + 1 < r to choose out two answer, then compare it to the target. If none equaled, return -1.
#
# Here is how we choose which half to continue the search.
# When nums[mid] > nums[r], we know that the pivot point must be in the right half. Then the left half is sorted. Based on this, we check if target locates in the left half. Otherwise it is in the right half.
# The same stragegy follows if nums[mid] < nums[r].


