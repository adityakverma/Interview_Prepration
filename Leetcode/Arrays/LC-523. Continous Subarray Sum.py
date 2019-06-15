
# I tried to do in your solution, and I changed process 2:
# we keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary, return True if we’ve seen a cumulative sum % k at least 2 indices before, or sum % k == 0 but num % k != 0, which means the sum of previous numbers match n*k.


# class Solution:
#     def checkSubarraySum(self, nums, k):
#         if k == 0:
#             for i in range(len(nums)-1):
#                 if nums[i] == 0 and nums[i+1] == 0:
#                     return True
#             return False
#
#         mod_list = dict()
#         mod = 0
#         for num in nums:
#             mod = (mod + num) % k
#             if (mod in mod_list) or (num % k != 0 and mod == 0):
#                 return True
#             mod_list[mod] = 1
#         return False

# ------------------------------------------------------------------------------

    #
    # If k == 0, then search for any consecutive pair of 0s.
    # Else, we will keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary. We will return True if we've seen a cumulative sum % k at least 2 indices before.
    #
    # This means that there is a subarray that has a sum(subarray) % k == 0 and that subarray contains at least 2 elements.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False


# https://leetcode.com/problems/continuous-subarray-sum/discuss/99566/Simple-Python-(10-lines)-with-Explanation-58ms-O(n)-time-O(k)-space
