
# Tags: "dutch partitioning problem"

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

############################### dutch partitioning problem. ##########################

# The problem is called dutch national flag problem.
# THIS WLL HELP TO SOLVE PROBLEM IN O(N) TIME COMPLEXITY UNLIKE O(N^2)

# Gist below:
# a) Traverse from left to right
# b) Maintain the most recent position of 0 and the position of 2.
# c) When 0 is encountered move to the left and for 2 move to right. (increment/decrement the pointers accordingly)
# d) When 1 is encountered do nothing.

class Solution():

    # https://www.youtube.com/watch?v=BOt1DAvR0zI
    def sortColors(self, A):
        low = mid = 0
        high = len(A) - 1

        while mid <= high: # Swap low and mid - Move to Left

            if A[mid] == 0:
                A[low], A[mid] = A[mid], A[low]
                low += 1
                mid += 1

            elif A[mid] == 2: # Swap mid and high - Move to Right
                A[mid], A[high] = A[high], A[mid]
                high -= 1
                # Note: here we don't do mid += 1 because if after swap we got 0
                # at that position, so it again needs a swap and needs to push to
                # left with another swap. that's why we don't increment mid in this case.
            else: # else 1 remains in middle. Zeros move to left and 2's moves to right
                mid += 1
        return A

###### Also check : 905. Sort Array By Parity where have to filter just two types - even and odd.

    # https://leetcode.com/problems/sort-colors/discuss/26479/AC-Python-in-place-one-pass-solution-O(n)-time-O(1)-space-no-swap-no-count
    # AC Python in place one pass solution O(n) time O(1) space, no swap no count
    def sortColors_FYI(self, nums):  # Just FYI
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return nums


if __name__ == '__main__':

    nums = [2,0,2,1,1,0]
    s = Solution()
    print "\nSorted Colors are: ",s.sortColors(nums)


# ------------------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(1) In-place sorting

# Note: dutch partitioning is only possible here since we only need to
# sort three numbers/items (Red,White and Blue), else we would have used
# Quick Sort
