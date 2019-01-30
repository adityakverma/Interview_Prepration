
#     Base case: target == 0
#
#     Recursive case: target > 0
#     we try nums[i] as a candidate of current combination and decrease target by nums[i] (only if target >= candidates[i])


class Solution():

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # return and then pop ( which is backtracking)
        if target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, target -nums[i], i, path +[nums[i]], res)

    #---------------------------------------------------------------------

    def combinationSum_(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
                return  # return and then pop ( which is backtracking)
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans