

# First we applied the backtracking, then we realise we just need count, so removed the intermediate array where we push and pop
# So this no more remained backtracking ... but then it was TLE
# So next we applied DP and it was ACCEPTED.

# https://leetcode.com/problems/combination-sum-iv/discuss/189148/Python-solution

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}  # Top Down approach or Memoization 

        def combs(s):
            if s in memo:
                return memo[s]

            if s == 0:
                return 1

            r = 0
            for n in nums:
                if s - n >= 0:
                    r += combs(s - n)
            memo[s] = r
            return r

        return combs(target)

    ###############################################3333

    # https://leetcode.com/problems/combination-sum-iv/discuss/208608/Python-memoized-DP

    def combinationSum4_(self, nums, target):  # Bottom Up Approach
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target == 0:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target+1):    # One loop was needed anyways - even with memoization, but second loop needed because we are not doing recursive calls unlike top down, instead we are looping and building dp array from bottom to up.
            for num in nums:
                if i >= num:
                    dp[i] = dp[i] + dp[i-num]
            # print(dp)
        return dp[target]


# https://leetcode.com/problems/combination-sum-iv/discuss/218725/Python-DFS-Beats-92
# https://leetcode.com/problems/combination-sum-iv/discuss/154577/Python-solution-to-follow-up-question


