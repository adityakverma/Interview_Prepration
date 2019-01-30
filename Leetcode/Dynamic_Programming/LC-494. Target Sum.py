

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # base case:reach the end
        if len(nums )==0:
            if S== 0:
                return 1
            else:
                return 0
        # use it: take next number as pos
        A = self.findTargetSumWays(nums[1:], S - nums[0])

        # lose it: take next number as neg
        B = self.findTargetSumWays(nums[1:], S + nums[0])

        return A + B