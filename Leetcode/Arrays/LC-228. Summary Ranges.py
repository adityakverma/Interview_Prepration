

# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
# Example 2:
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


class Solution():

    # https://leetcode.com/problems/summary-ranges/discuss/63283/Python-solution-with-comments
    def summaryRanges1(self, nums):
        ans = []
        for i in range(len(nums)):
            # We are on the 1st number OR the number is not continuous with the previous number in nums. This will count both first and last element
            if i == 0 or nums[i] != nums[i - 1] + 1:
                ans.append(str(nums[i]))
            # The number we are on is not continuous with the next number in nums
            elif nums[i] != nums[i + 1] - 1:
                ans[len(ans) - 1] += '->' + str(nums[i])
        return ans

    # https://leetcode.com/problems/summary-ranges/discuss/63261/Python-Two-Pointers-O(n)
    # Two Pointer technique:
    def summaryRanges2(self, nums):
        i, j = 0, 0
        ans = []
        while i < len(nums) and j < len(nums):
            k = 0
            while j < len(nums) and nums[i] + k == nums[j]:
                j += 1
                k += 1
            if i + 1 == j:  # Checking the continuity of series, if not append ... else that range
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i]) + '->' + str(nums[j - 1]))
            i = j
        return ans

    # https://leetcode.com/problems/summary-ranges/discuss/63335/Simple-Python-solution
    def summaryRanges3(self,nums):
        if not nums:
            return []

        nums = nums + [nums[-1] + 2]
        res = []
        head = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:  # Since we are always checking number with previous one for comparision, so we are adding dummy.
                if head == nums[i - 1]:
                    res.append(str(head))
                else:
                    res.append(str(head) + "->" + str(nums[i - 1]))
                head = nums[i]
        return res

if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9,12]
    s = Solution()
    print "\nGiven Range  : ",nums
    print "\nSummary Range1:",s.summaryRanges1(nums)
    print "\nSummary Range2:",s.summaryRanges2(nums)
    print "\nSummary Range3:",s.summaryRanges3(nums)



