

# -------------------------------------------------------------------------------------
# LC-1. Two Sum

class Solution(object):

    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False

        dic = {}  # For saving Indexes. Making dic of possible difference with target. If present then return that value's index along with i
        for i in range(len(nums)):

            if nums[i] in dic.keys():  # Or just use dic   # If present then return that value's index along with i
                return [dic[nums[i]], i]
            else:
                dic[target - nums[
                    i]] = i  # Making dic of possible difference with target as key AND corrosponding index as value.

        # Algorithm:
        # =========
        # Step-1: For each array element - Keep making dic of possible difference with target as key AND corrosponding index as value.
        # Step-2: Now if this key is already present while we iterate through array elements then return those indexes - [dic[num[i]],i]
        # Step-3: Else keep doing step-1

# -------------------------------------------------------------------------------------
# 15. 3Sum

    def threeSum(self, nums):
        res = []
        nums.sort() # So we can skip same values, since we need to find all solution unique sets.

        for i in xrange(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]: # Keep skipping if same numbers, since we need unique solution sets
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < 0:   # Meaning move start to bigger in front so we can get s >= 0
                    start += 1
                elif s > 0: # Meaning sum s is bigger so try reducing from end.
                    end -= 1

                else:
                    res.append((nums[i], nums[start], nums[end]))

                    # Below two while loops are just an extra check, where before moving to next unique number we just skip same values.
                    # we need to move the left and right pointers to the next different numbers, so we do not get repeating result.

                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1  # Move start to next bigger number (note array is sorted)
                    end -= 1    # Move end to lesser number since array is sorted
        return res

# -------------------------------------------------------------------------------------
# 18. 4Sum


    def fourSum(self, nums, target):

        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # NOW YOU EITHER CALL threeSum(nums,target) or below. Note in LC-15 target was 0
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                start = j + 1
                end = len(nums) - 1

                while (start < end):
                    sum = nums[i] + nums[j] + nums[start] + nums[end]

                    if sum < target:
                        start = start + 1
                    elif sum > target:
                        end = end - 1

                    else:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        end = end - 1

                        while start < end and nums[start] == nums[start - 1]:
                            start = start + 1
                        while start < end and nums[end] == nums[end + 1]:
                            end = end - 1

        return res

# -------------------------------------------------------------------------------------
# 4. Median of Two Sorted Arrays
# taking advantage of devide and conquer method. The time complexity is o(log(n) +log(m)).

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

# -------------------------------------------------------------------------------------
# LC-238. Product of Array except Self.

    def productExceptSelf(self, nums):

        res = [1] * len(nums)

        p = 1
        for i in range(len(nums)): # from left to right
            res[i] *= p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1): # from right to left
            res[i] *= p
            p *= nums[i]

        return res

# -------------------------------------------------------------------------------------
# 53. Maximum Subarray : Simplest form of DP

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


# -------------------------------------------------------------------------------------
# 56. Merge Intervals

    # Definition for an interval.
    class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e

    class Solution(object):

        def merge(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """
            intervals.sort(key=lambda x: x.start)
            ret = []

            for itv in intervals:
                start, end = itv.start, itv.end

                if not ret or ret[-1].end < start:
                    ret.append(Interval(start, end))  # Append it to result now. Later it will be adjusted for end if required.
                else:
                    ret[-1].end = max(ret[-1].end, end)
            return ret

# -------------------------------------------------------------------------------------
# 42 - Trapping Rain Water
 # Submitted on 3/26/2019

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # The water we trapped depends on the left side and right side which has the max height,

        if not height or len(height) < 3:
            return 0

        water = 0
        LMax = [0] * len(height)
        RMax = [0] * len(height)

        LMax[0] = height[0]
        for i in range(1, len(
                height)):  # Note in range last one is not considered. Also last one will not hold any water for sure.
            LMax[i] = max(height[i], LMax[i - 1])  # Max from left to right

        RMax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            RMax[i] = max(height[i], RMax[i + 1])  # Max from right to left

        # print LMax, RMax

        for i in range(len(height) - 1):
            water += min(LMax[i], RMax[i]) - height[i]

        return water

# -------------------------------------------------------------------------------------
# 695. Max Area of Island

    def maxAreaOfIsland(self, grid):

        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            if (0 <= x and x < n) and (0 <= y and y < m) and grid[x][y]:
                grid[x][y] = 0
                return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1
            return 0

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area

# -------------------------------------------------------------------------------------
# 283. Move Zeroes

    def moveZeroes(self, nums):

        self.zero = 0  # records the position of "0"

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[self.zero] = nums[i]
                self.zero += 1

        while self.zero < len(nums):
            nums[self.zero] = 0
            self.zero += 1

        return nums

# -------------------------------------------------------------------------------------
# 11. Container With Most Water

    def maxArea(self, height):

        # Approach  (Two Pointer Approach)
        i, j = 0, len(height) - 1
        result = 0

        while (i < j):
            result = max(result, min(height[i], height[j]) * (j - i))
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return result

# -------------------------------------------------------------------------------------
# 16. 3Sum Closest

# Same algorithm as 3sum problem, where we sort nums, then use two pointers to check all the possible combinations,
# while fixing one element.


    def threeSumClosest(self, num, target):

        num.sort()
        result = num[0] + num[1] + num[2]

        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1

            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum    # We keep updating result with least sum every time in while loop

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

# Similar to 3 Sum problem, use 3 pointers to point current element, next element and the last element.
# If the sum is less than target, it means we have to add a larger element so next element move to the next.
# If the sum is greater, it means we have to add a smaller element so last element move to the second last element.
# Keep doing this until the end. Each time compare the difference between sum and target, if it is less than
# minimum difference so far, then replace result with it, otherwise keep iterating.

# -------------------------------------------------------------------------------------
# 457. Circular Array Loop

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def getIndex(i):
            n = len(nums)
            return (i + nums[i] + n) % n

        # start from every position in the array
        for i, val in enumerate(nums):
            if val == 0:
                continue

            # slow/fast pointer
            j = i
            k = getIndex(i)

            # as long as moving in the same direction - either forward or backward
            while nums[k] * nums[i] > 0 and nums[getIndex(k)] * nums[i] > 0:
                if j == k:
                    # check for loop with only one element. Meaning len(nums) ==1 so loop of 1 element is not allowed.
                    if j == getIndex(j):
                        break
                    return True

                j = getIndex(j)
                k = getIndex(getIndex(k))

            # loop was either not found or if found, it was not unidirectional
            # traverse entire loop again from start (i) and mark the ones which have been visited. Set all element along the way to 0
            # This means this path doesn't have loop, so try for next value of i ( from outer for loop)
            j = i
            while nums[j] * val > 0:
                next = getIndex(j)
                nums[j] = 0
                j = next

        return False

# Concept:
# ========
# # Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. Use a
# slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. If there
#  is a loop (fast == slow), we return true, else if we meet element with different directions, then the
# search fail, we set all elements along the way to 0. Because 0 is fail for sure so when later search meet
#  0 we know the search will fail.

# -------------------------------------------------------------------------------------
# 713. Subarray Product Less Than K

# SLIDING WINDOW:
# Two pointer O(n) time O(1) space:
# Initialize a left index j = 0 and a right index i = 0. As we iterate i over range(len(nums)),
# we keep updating res, the cumulative product of all entries from j to i. As soon as res >= k,
# we move the left index to the right until res < k. The length i - j + 1 is then the number of subarrays
# ending with i where the product of all elements in the subarray is less than k.

    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# -------------------------------------------------------------------------------------
# 905. Sort Array By Parity

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # In-place : Idea is simple - if odd is on the left and even is on the right, then we swap

        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:  # If left side element is odd then swap it with right ones. No pointers moved. Just readjust them.
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1  # If left side element is even itself, then simply move left pointer
            if A[j] % 2 == 1: j -= 1  # IF right side element is odd itself, then simply move right pointer

        return A

# -------------------------------------------------------------------------------------
# 287. Find the Duplicate Number : Important problem to apply Binary Search or Cycle Detection Algo

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1

            if count > mid:
                high = mid - 1
                # print "lower half. low & high are", low, high
            else:
                low = mid + 1
                # print "upper half. low & high are", low, high

        return low

#  This solution is based on binary search.
# At first the search space is numbers between 1 to n. Each time I select a number mid (which is the one
# in the middle) and count all the numbers equal to or less than mid. Then if the count is more than mid,
# the search space will be [1 mid] otherwise [mid+1 n]. I do this until search space is only one number.

# -------------------------------------------------------------------------------------
# 34. Find First and Last Position of Element in Sorted Array: Earlier called "Search Ranges"

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)?page=2
# Using Binary Search:

    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

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

# -------------------------------------------------------------------------------------

# 35. Search Insert Position in SORTED list. # Note: Sorted itself hints use of Binary Search

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)

        if target < nums[0]:
            return 0

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

# -------------------------------------------------------------------------------------
# 697. Degree of an Array

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

# https://leetcode.com/problems/degree-of-an-array/solution/#

# -------------------------------------------------------------------------------------
# 120. Triangle

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    # https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up).

# -------------------------------------------------------------------------------------
# 724. Find Pivot Index

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, sum(nums)

        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

    # Time: O(n)
    # Space: O(1)

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

#  -------------------------------------------------------------------------------------






























