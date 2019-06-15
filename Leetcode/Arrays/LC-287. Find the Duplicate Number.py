

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate
# number, find the duplicate one.

# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
#
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# =================================================================================================


# Excellent Binary Search Solution:  O(nlogn)
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation):-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array


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


'''
This solution is based on binary search.

At first the search space is numbers between 1 to n. Each time I select a number mid (which is the one in the middle) and count all the numbers equal to or less than mid. Then if the count is more than mid, the search space will be [1 mid] otherwise [mid+1 n]. I do this until search space is only one number.

Let's say n=10 and I select mid=5. Then I count all the numbers in the array which are less than equal mid. If the there are more than 5 numbers that are less than 5, then by Pigeonhole Principle (https://en.wikipedia.org/wiki/Pigeonhole_principle) one of them has occurred more than once. So I shrink the search space from [1 10] to [1 5]. Otherwise the duplicate number is in the second half so for the next step the search space would be [6 10].
'''
#------------------------

# Regular logic
'''
def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
'''

#---------------------------

# Cycle Detection Solution - O(n)
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
# https://leetcode.com/problems/find-the-duplicate-number/solution/#

'''
def findDuplicate(self, nums):
    # Find the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1
'''

