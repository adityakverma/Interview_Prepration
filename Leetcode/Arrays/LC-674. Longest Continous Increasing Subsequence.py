#  Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.

class Solution(object):

    # My Solution: Similar to LC-485
    def findLengthOfLCIS(self, nums):
        if len(nums)<1: return 0
        max_cnt = count = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
                max_cnt = max(max_cnt, count)
            else:
                count = 1
        return max_cnt

if __name__ == '__main__':
    arr = [1,3,5,4,7,6,8,9,10,11]
    s = Solution()
    print "\nMax count for LCIS is: ",s.findLengthOfLCIS(arr)
