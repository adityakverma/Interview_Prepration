
##########################################################################################

# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -infinity.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
#
# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.

##########################################################################################


def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)
    import sys
    minus_infintiy = -(sys.maxint - 1)

    nums = [minus_infintiy] + nums + [minus_infintiy]

    for i in range(1, n + 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i - 1



# For Binary Search Solution: See below:



# Lets say you have a mid number at index x, nums[x]
# if (num[x+1] > nums[x]), that means a peak element HAS to exist on the right half of that array, because (since every number is unique) 1. the numbers keep increasing on the right side, and the peak will be the last element. 2. the numbers stop increasing and there is a 'dip', or there exists somewhere a number such that nums[y] < nums[y-1], which means number[x] is a peak element.
#
# This same logic can be applied to the left hand side (nums[x] < nums[x-1]).

# ---
# Most people have figured out the binary search solution but are not able to understand how its working. I will try to explain it simply. What we are essentially doing is going in the direction of the rising slope(by choosing the element which is greater than current). How does that guarantee the result? Think about it, there are 2 possibilities.a) rising slope has to keep rising till end of the array b) rising slope will encounter a lesser element and go down.
# In both scenarios we will have an answer. In a) the answer is the end element because we take the boundary as -INFINITY b) the answer is the largest element before the slope falls. Hope this makes things clearer.

class Solution():

    def findPeakElement(self, nums):    # This is good solution using Divide and Conquer. This solution runs well on LC, but doesn't submits.
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)/2  # Better way is: m = l + (r - l) / 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l

    # [Aditya]: This is Solution for LC 153, which I converted to this solution just by flipping greater sign in line47
    def findMin(self, nums):    # This is good solution using Divide and Conquer
        if len(nums) == 1:
            return nums[0]

        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            if nums[m] < nums[j]:  # Note this was solution for LC-153, I just flipped greater sign as it turned into this solution
                i = m + 1
            else:
                j = m
        return [i,nums[i]]

if __name__ == '__main__':

    nums = [1,2,1,3,5,6,4]
    s = Solution()
    print "\nPeak Element is at index :",s.findPeakElement(nums)
    print "\nPeak Element is at index and its value is  %d:", s.findMin(nums)


# Time complexity : O(log(n)) We reduce the search space in half at every step. We reduce the search space in half at every step
# Space complexity : O(1). Constant extra space is used.


