
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# ------------------------------------------------------------------------------------------

# Bottom-up approach or Tabulation method.
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/164156/Python-or-DP-tm
# Explanation: https://www.youtube.com/watch?v=CE2b_-XfVDk&t=222s

class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# > Time Complexity O(N^2)
# > Space Complexity O(N)

if __name__ == '__main__':
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print "\nLongest Increasing subsequence: \n",s.lengthOfLIS(nums)

# How to reduce the time complexity by nlogn .. we need to use binary seaarch
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step
