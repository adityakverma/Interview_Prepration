
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# ----------------------------------------------------------------------

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, size):
            if len(tmp) == size:
                ans.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue

                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums) # Use an extra boolean array to indicate whether the value is added to list.
        nums.sort()   # Sort the array "int[] nums" to make sure we can skip the same value. when a number has the same value with its previous, we can use this number only if his previous is used
        backtrack([], len(nums))
        return ans

    # Previous solution LC-46 will also work here, but gives duplicate permutations also. So we use boolean visited array and sort it.
    # Duplication happens when we insert the duplicated element before and after the same element, to eliminate duplicates, just insert only after the same element.
    # I think boolean array is main trick which maintains the visited elements.
    # Sorting is another trick, which ...

    

