


# The idea is to order the envelopes and then calculate the longest increasing
# subsequence (LISS). We first sort the envelopes by width, and we also make
#  sure that when the width is the same, the envelope with greater height comes
# first. Why? This makes sure that when we calculate the LISS, we don't have a
# case such as [3, 4] [3, 5] (we could increase the LISS but this would be wrong
# as the width is the same. It can't happen when [3, 5] comes first in the ordering).


# Example:
#
# input
#
# [[5,4],[6,4],[6,7],[2,3]]
#
# sort by increasing widths, then decreasing heights:
#
# [[2,3],[5,4],[6,7],[6,4]]
#
# Get the heights:
#
# [3,4,7,4]
#
# Find the length longest increasing subsequence:
#
# [3,4,7]

#         # sort first by increasing width
#         # within each subarray of same-width envelopes
#         # sort by decreasing height
#         envs.sort(key=lambda (w,h): (w,-h))
# =============================================================================

class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        l = len(envelopes)
        if l == 1:
            return 1

        # Let's sort with increasing order of width x[0], but if two envelope have same width then sort with decreasing height x[1].
        envelopes.sort(key=lambda x: ( x[0], -x[1]))  # because when the width is the same, the envelope with greater height comes first.

        width = []
        for i in envelopes:
            width.append(i[1])

        res = self.longestSubsequence(width)
        # the problem became LIS after sort(width)

        return res

    def longestSubsequence(self, nums):
        """
        return type: int (number of longest subsequence)
        """
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# ------------

# Example:
#
# input
#
# [[5,4],[6,4],[6,7],[2,3]]
#
# sort by increasing widths, then decreasing heights:
#
# [[2,3],[5,4],[6,7],[6,4]]
#
# Get the heights:
#
# [3,4,7,4]
#
# Find the length longest increasing subsequence:
#
# [3,4,7]

         # sort first by increasing width
         # within each subarray of same-width envelopes
         # sort by decreasing height
         # envs.sort(key=lambda (w,h): (w,-h))

############################################################################
# https://leetcode.com/problems/russian-doll-envelopes/discuss/82754/Python-solution-based-on-LIS


# def maxEnvelopes(self, envelopes):
#     """
#     :type envelopes: List[List[int]]
#     :rtype: int
#     """
#     if not envelopes:
#         return 0
#
#     l = len(envelopes)
#     if l == 1:
#         return 1
#
#     envelopes.sort(
#         cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
#     # sort the envelopes by width because they need to be inorder before consider the heigths or versa
#
#     width = []
#     for i in envelopes:
#         width.append(i[1])
#
#     res = self.longestSubsequence(width)
#     # the problem became LIS after sort(width)
#
#     return res
#
#
#
# def longestSubsequence(self, nums):
#     """
#     return type: int (number of longest subsequence)
#     """
#     if not nums:
#         return 0
#     l = len(nums)
#     res = []
#
#     for num in nums:
#         pos = self.binarySearch(num, res)
#         if pos >= len(res):
#             res.append(num)
#         else:
#             res[pos] = num
#
#     return len(res)
#
#
#
# def binarySearch(self, target, nums):
#     """
#     return type: int (ceiling of the insert position)
#     """
#     if not nums:
#         return 0
#
#     l = len(nums)
#     start = 0
#     end = l - 1
#
#     while start <= end:
#         half = start + (end - start) // 2
#         if nums[half] == target:
#             return half
#         elif nums[half] < target:
#             start = half + 1
#         else:
#             end = half - 1
#
#     return start

###############################################################################