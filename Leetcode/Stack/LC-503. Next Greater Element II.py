
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element.
# The Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly to
# find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# ===============================================================================

class Solution():

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1]*len(nums)
        n = len(nums)

        for i in xrange(0, 2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                top = stack.pop()
                if res[top] == -1:
                    res[top] = nums[i%n]
            stack.append(i%n)
        return res

# https://leetcode.com/problems/next-greater-element-ii/discuss/98328/Python-solution-with-detailed-explanation

# Algorithm
# =========
#     Stack for next greater element: Suppose we have a decreasing sequence followed by a greater number. For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence.

#     Handling duplicates in input: Push the index and value tuple on the stack instead of just the value. This makes sure duplicated elements are correctly handled. Example:[100,1,11,1,120,111,123,1,-1,-100] - we need to have the right answer for both 1s.

#     Handling circular array: Process it twice. Example: [5,4,3,2,1]. By processing it twice, you are essentially doing: [5,4,3,2,1]+[5,4,3,2,1]. Typical pattern to solve circular array problems is to extend the original array to twice length, 2nd half has the same element as first half. Then everything become simple.

#     https://discuss.leetcode.com/topic/77881/typical-way-to-solve-circular-array-problems-java-solution
