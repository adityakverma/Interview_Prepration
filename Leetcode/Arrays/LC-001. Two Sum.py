

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Idea is,  we save the difference of taget- current number in special hash. During loop iteration, if we find current array element is present in hash then we return those pair.

        if len(nums) <= 1:
            return False

        dic = {}  # Making dic of possible difference with target.  Since the hash table reduces the look up time to O(1)

        for i, n in enumerate(nums):
            if n in dic:  # If present then return that value's index along with i
                return [dic[n], i]
            dic[target - n] = i

# Complexity Analysis:
# Time complexity : O(n). We traverse the list containing n elements exactly twice. Since the hash table reduces the look up time to O(1), the time complexity is O(n).
# Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nnn elements.


# ===============================================================
# Tags: Array, Hash Table, Facebook, MS, Amazon, LinkedIn, Apple
# ===============================================================
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution():

    # Time Complexity : O(n square)
    def twoNum(self,num,target):
        if len(num) <= 1:
            return False
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i]+num[j] == target and num[i] != num[j]:
                    return [i,j]

    # Time Complexity : O(n)
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            buff_dict[target - nums[i]] = i

    def twoSum2(self, nums, target):
        dic = {}  # Making dic of possible difference with target. If present then return that value's index along with i
        for i, n in enumerate(nums):
            if n in dic:            # If present then return that value's index along with i
                return [dic[n], i]
            dic[target - n] = i

# driver function
if __name__ == '__main__':

    num = [2,7,11,15]
    target = 9
    s = Solution()

    print s.twoNum(num, target)
    print s.twoSum(num, target)
    print s.twoSum2(num, target)
