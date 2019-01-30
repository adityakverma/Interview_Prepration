
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1 (max is 2), then 3 steps to the last index.
#
# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
# ---------------------------------------------------------------------------------------------------

# This is a dynamic programming[1] question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:
#
#     Start with the recursive backtracking solution
#     Optimize by using a memoization table (top-down[3] dynamic programming)
#     Remove the need for recursion (bottom-up dynamic programming)
#     Apply final tricks to reduce the time / memory complexity

# IMPORTANT LINK - MUST SEE. HELPS TO CLEAR CONCEPTS OF DP, GREEDY AND BACKTRACKING. <============
# https://leetcode.com/problems/jump-game/discuss/215746/4-Possible-Solutions-with-Comments-in-Python-3
# https://leetcode.com/problems/jump-game/discuss/182034/Difference-Between-DP-and-Greedy
# https://leetcode.com/problems/jump-game/solution/


# ----------------------------------------------------------------------------------------------------------
# GREEDY METHOD: Looking from the start and selecting the locally optimum in the hope of reaching global optimum
# --------------
# https://leetcode.com/problems/jump-game/discuss/114802/Python-DP-O(n)-solution-accepted

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True

        # define the state dp[i] as the maximum index one can jump after reach index i.

        dp    = [0]*len(nums)  # Dp[i] will have maximum jump it can make to reach end.
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1]<i:   # Meaning you cannot reach to position i since value of previous result dp[i-1] is less than current position.
                return False
            dp[i] = max(dp[i-1], i + nums[i]) # Else update dp
        return dp[-1]>=len(nums)-1

# Note: Here we are doing current index plus value at that index because it will tell where we can reach maximum by that.

# --------------------------------------------------------------
# https://leetcode.com/problems/jump-game/discuss/21037/Very-Simple-O(n)-Python-Solution-w-O(1)-Space-91.35

class Solution_(object):
    def canJump(self, nums):

        last = len(nums)
        max = 0

        for i in xrange(last):
            if max < i:         # Meaning you cannot reach to position i since value of max till date is less than i, so return False
                return False

            if i + nums[i] > max: # Otherwise Update max
                max = i + nums[i]

        return True

# Explanation:
#
# We keep track of the maximum number of spaces we can reach as we iterate through the array.
# If the current index is greater than the max, then with the numbers we have seen so far, there is no way for us to reach anything beyond the current number and thus we are done.
# If the current index is reachable, then we see if we can get a better max. If the (current index) + (max number of spots we can jump from current index) > max, we update the max.
# If we finish the loop that means the last index is reachable and we are done.
# ---------------------------------------------------------------------------------------------

# https://leetcode.com/problems/jump-game/discuss/182034/Difference-Between-DP-and-Greedy
# https://leetcode.com/problems/jump-game/discuss/216672/python-forward-greedy-solution


# Again python forward greedy solution
class Solution__(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dist = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                dist = i + nums[i]
                if dist > max_dist:
                    max_dist = dist
            else:
                if max_dist <= i and i != len(nums)-1:
                    return False
        return True

# ----------------------------------------------------------------------------------------------

