
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
import collections
from collections import defaultdict
class Solution():

    # My Solution Brute-force
    def Total_SubarraySumWithK_LC560(self,nums,k):  # 57 / 80 test cases passed.

        if len(nums)<1: return 0
        subarr_cnt = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    subarr_cnt += 1
                    break
        return subarr_cnt


    # Main idea: Number of ways you can reach "k" is equal to number of ways you can reach "cur_sum - k". Checkout figure below
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book
    def subarraySum(self, nums, k):

        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1
        cur_sum = 0
        cnt = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum - k in sum_cnt:
                cnt += sum_cnt[cur_sum - k]

            sum_cnt[cur_sum] += 1

        return cnt



    # Same as above, just use collection instead of native dict.
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
    def subarraySum2(self, A, K):
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su - K]
            count[su] += 1
        return ans

if __name__ == '__main__':
    nums = [1, 1, 1, 4, 3, 2]
    nums1 = [1, 2, 1, 2, 1]
    nums2 = [0,0,0,0,0,0,0,0,0,0]
    k = 5
    k1 = 3
    k2 = 0
    s = Solution()
    print "\nTotal number of continuous subarrays whose sum equals to %d is: %d" %(k1,s.Total_SubarraySumWithK_LC560(nums1,k1))
    print "\nTotal number of continuous subarrays whose sum equals to %d is: %d" %(k1,s.subarraySum(nums1,k1))

# https://leetcode.com/problems/subarray-sum-equals-k/discuss/102119/Super-Simple-Python

# EXPLANATION:
# ============
# you basically store the # of occurrence for each "prefix" sum of the array up to a given index.
#
# For example,
#
# if the array is [1 3 4 13]
# our prefix sum dictionary will contain these elements at each index:
# before start: {0:1} -> 0 sum would be the equivalent of an empty array
# index 0: {0:1, 1:1} -> prefix sum up to and including index 0 is 1
# index 1: {0:1, 1:1, 4:1} -> prefix sum up to and including index 1 is 4. If you're confused at this point, we're just storing the sum up to each index
# index2: {0:1, 1:1, 4:1, 8:1} -> prefix sum up to index 2
# index3: {0:1, 1:1, 4:1, 8:1, 21:1} prefix sum up to index 3 == 21
#
# Now during the same iteration we can check if there is a prefix array we can discard to obtain our desired target of k. For example if k=7 in our example above when we arrive at index 2, our sum will be 8 but we can see that there is a prefix sum of 1 in the array according to our hashmap. Thus we can deduce that there is a contiguous subarray of sum 7 and this can be achieved by getting rid of the prefix array of sum of 1 in our current window. To visually illustrate:
#
# our window at index2: [1 3 4]
# prefix array with sum of 1: [1]
# valid subarray with sum of k [1 3 4] - [1] = [3 4]
#
# Don't pay attention to the syntax of the above equation as it's just to illustrate the concept of taking out the prefix array.
#
# Another example would be if k = 17, then
#
# window at index3 : [1 3 4 13] with a sum of 21. Since target is 17, we need to see if there's a prefix array that sums to 4.
# According to our hashmap, at index1 we have a prefix array of sum of 4: [1 3]
# thus: [1 3 4 13] - [1 3] = [4 13] which sums to 17
# ------------------------------------------------------------------------------

# 713. Subarray Product Less Than K : Similar Problem
# https://leetcode.com/problems/subarray-product-less-than-k/description/
