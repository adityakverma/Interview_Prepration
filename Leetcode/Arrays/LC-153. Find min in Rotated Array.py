
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48619/9-line-python-clean-code

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
# You may assume no duplicate exists in the array.
#
# Example 1:
# Input: [3,4,5,1,2]
# Output: 1
# --------------------------------------------------------------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) / 2

            if nums[mid] > nums[end]:  # then lowest in second half
                start = mid + 1
            else:
                end = mid

        return nums[start]

    '''
    Classic binary search problem.

Looking at subarray with index [start,end]. We can find out that if the first member is less than the last member, there's no rotation in the array. So we could directly return the first element in this subarray.

If the first element is larger than the last one, then we compute the element in the middle, and compare it with the first element. If value of the element in the middle is larger than the first element, we know the rotation is at the second half of this array. Else, it is in the first half in the array. '''















# ------------------------------------------------------------------


class Solution():
    def MinElementRoataedArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-1):
            if nums[i+1]< nums[i]:
                return nums[i+1]
        return nums[0]

    def findMin(self, nums):    # This is good solution using Divide and Conquer
        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) / 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low],low

    def findMin1(self, nums):
        return min(nums)

    def findMin2(self, nums):
        min=nums[0]
        for i in nums:
            if(i<min):
                min=i
                return min
        return min

if __name__ == '__main__':

    nums = [5,6,7,8,1,2,3,4]
    s = Solution()
    print "\nMinimum Element in Rotated array is: ", s.MinElementRoataedArray(nums)
    print "\nMinimum Element in Rotated array and its position is: ", s.findMin(nums)


# NOTE:
# Yes, in fact this is a simple solution. But note the time complexity of this algorithm. In the worst case it has to scan the entire list to find out the minimum value (O(n)). So the better solution would be a Divide and Conquer based approach which result in logarithmic time complexity and perform much better for any size of inputs. Binary Search is log (n) and a modified version of binary search can be used here !
# This is nice for small arrays, because it's O(n). As the size of the array increases, this is a very bad solution. Binary Search O(log n) scales better than Linear Search O(n).
