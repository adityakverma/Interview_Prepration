
# # Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# ========================================================================================================


class Solution():

    # https://leetcode.com/problems/search-for-a-range/discuss/14869/Python-easy-solution-with-explanation
    # Using Binary Search with time complexity log(n)
    def searchRange_LC034(self, nums, target):

        #
        start = 0
        end = len(nums) - 1
        result = []

        # Search for the left one
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        result.append(start)

        # Search for the right one
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        result.append(end)

        if result[0] > result[1]:
            return [-1, -1]
        else:
            return result

    # https://leetcode.com/problems/search-for-a-range/discuss/14706/Beats-100-Python-submission
    def searchRange(self, nums, target):
        n = len(nums)
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)/2
            if nums[m] < target: l = m+1
            else: r = m
        if nums[l] != target: return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)/2+1
            if nums[m] == target: l = m
            else: r = m-1
        right = l
        return [left, right]

if __name__ == '__main__':

    s = Solution()
    InputArr = [5,7,7,8,8,10]
    target = 8
    print "\nSearch Range:",s.searchRange_LC034(InputArr,target)
    print "\nSearch Range:",s.searchRange(InputArr,target)

###########################################################################################

def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return [-1, -1]

    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1   # Note: We added 1 here, so Make mid biased to the right
            if nums[m] > target:  # Comparision reversed
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]

