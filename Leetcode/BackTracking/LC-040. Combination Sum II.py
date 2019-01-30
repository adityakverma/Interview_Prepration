

# ---------- IDEA --------------------
#     Base case: target == 0
#
#     Recursive case: target > 0
#     we try nums[i] as a candidate of current combination and decrease target by nums[i] (only if target >= candidates[i])


class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort(reverse=True)
        self.backtrack(nums, 0, [], target, res)
        return res

    def backtrack(self, nums, start, cur, target, res):  # Taget is new parameter here compared to other problems

        if target == 0:
            res.append(cur[:])
            return  # return back and then pop (which is backtracking)

        elif target > 0:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[
                            i - 1]:  # i>start is actually making sure- ONLY get 1st instance (& no dups)
                    continue
                cur.append(nums[i])
                self.backtrack(nums, i + 1, cur, target - nums[i], res)
                cur.pop()


    # Couple os points:
    # =================

    # 1. We increment the i during recursive call to conside next position.
    # 2. To elimate the dups from the input, we sort and then compare with previous ( is same then skip/continue. Line 21)
    # 3. There is no visited array here unlike LC-47 because here order dosen't matter. Its not permuation. Its combination. OR
    #    Way this is different from LC-47 (Permutation problem-II) - Here we are not tracking positions( or order). So no visited array.
    # 4. See how we have considered target parameter which reduces on every recursive calls. This is new parameter
    # 5. Make sure we return (line 17), so when condition is met, append answer and return and pop ( which is backtracking)
    # 6. See how this is different from LC-39 where we are not incrementing i because same input can be considered multiple times.
    # 7. LC-39 and 40 are different in same way like (LC-46 is with 47) and so is (LC-78 is with 90)



