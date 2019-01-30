
# Given an array of integers nums and a positive integer k, find whether
# it's possible to divide this array into k non-empty subsets whose sums
# are all equal.
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4),
# (2,3), (2,3) with equal sums.

# =========================================================================

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/129855/Python-easy-to-understand-and-clean
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/157625/python-solution-beats-10040ms

# Need to solve this by myself again


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visit = [0 for i in range(len(nums))]
        target= sum(nums) // k
        def DFS(k, fromindex, cursum):
            if k == 1 and cursum == target:
                return True
            if cursum == target:
                return DFS(k-1, 0, 0)
            else:
                for i in range(fromindex, len(nums)):
                    if nums[i] + cursum <= target and not visit[i]:
                        visit[i] = 1
                        if DFS(k, i + 1, cursum + nums[i]):
                            return True
                        visit[i] = 0
                return False
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        return DFS(k, 0, 0)

###########################################################################3

class Solution_:
    def canPartitionKSubsets(self, nums, k):
        if k> len(nums):
            return False
        if k==1:
            return True
        total=sum(nums)
        if total%k!=0:
            return False
        else:
            target=int(total//k)
        nums.sort(reverse=True)
        visited=[0 for i in range(len(nums))]
        return self.dfs(nums,0,k,visited,0,target)

    def dfs(self,nums,start,k,visited,cur_sum,tar):
        if cur_sum>tar:
            return False
        if k==1:
            return True
        if cur_sum==tar:
            return self.dfs(nums,0,k-1,visited,0,tar)
        for i in range(start,len(nums)):
            if not visited[i] and cur_sum+nums[i]<=tar:
                visited[i]=1
                if self.dfs(nums,i+1,k,visited,cur_sum+nums[i],tar):
                    return True
                visited[i]=0
        return False
