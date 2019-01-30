
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


# Example 3:
# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 8 ->9)  # From 1, we jump 1 step to 3. From 3 we jump only 2 jumps as 3 is max,
# and reach 8, then from 8 we take just 1 steps and reach 9 ( note 8 is max, so we can just any number
# of steps with 8). Finally from 9 we reach to end by jumping 6 steps.

# Tushar Roy
# https://www.youtube.com/watch?v=cETfFsSTGJI&t=0s&index=23&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr  <=== I didn't check
# ----------------------------------------------------------------------------------------------

# https://leetcode.com/problems/jump-game-ii/discuss/18035/Easy-Python-Greedy-solution-with-explanation
# The basic strategy: we iterate through the array, and while we do this, we find the minimum number of jumps it takes to get to where we are. We do this by incrementing our jumps counter whenever a new jump is needed to get us to the current index. This involves keeping track of the furthest point our last jump could have taken us. Also, the current jump can originate from any of the indices reachable by the previous jump, thus we check these places (as we are going through the loop) to find which index in our current jump takes us the furthest.
# Once we reach the end of the array, we know the minimum number of jumps it takes to get to the end.

class Solution(object):  # ACCEPTED - GREEDY ALGO
    def jump(self, nums):
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0

        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i]) # nums[i] gives the furthest we can go during the current jump, and we update current_jump_max with it.
            # Note 1
            if i == previous_jump_max:  #  If our current index reaches the furthest point our last jump could have gone, then a new jump would be needed to get to any of the indices after it. Thus we increment jumps
                jumps += 1
                previous_jump_max = current_jump_max # since the current jump is now a new jump, we make previous_jump_max be current_jump_max, that is, our previous jump can now get us as far as current jump max, since we've now started a new jump.
                # Note 2
        return jumps


# Note 1: We want to find what's the furthest we can go from our current jump. It may be that an index previous to this one in our current jump could have had a longer reach than our current index, if so, that would have been stored in current_jump_max during earlier iterations of this loop, otherwise, nums[i] gives the furthest we can go during the current jump, and we update current_jump_max with it.
# At the beginning, no previous jumps have been made, so that the max is automatically the number of jumps stored in nums[0]. In general the current jump would include all the indices that were reachable from the last jump: we want to find the greatest distance we can go given all these possible starting points.
# Note 2: If our current index reaches the furthest point our last jump could have gone, then a new jump would be needed to get to any of the indices after it. Thus we increment jumps, and since the current jump is now a new jump, we make previous_jump_max be current_jump_max, that is, our previous jump can now get us as far as current jump max, since we've now started a new jump. Jumps will thus increment only when a new jump is necessary to reach an index. Once we've iterated through the array, jumps store the minimum needed to get to the end.
