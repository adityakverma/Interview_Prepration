

# https://leetcode.com/problems/majority-element/discuss/51864/Python-solution(sorting-hashmap-moore-voting-bit-manipulation)

# Given an array of size n, find the majority element. The majority element is the element that appears more than  n/2 times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)/2]

    # Boyer Moore majority vote algorithm. Refer to
    def majorityElement_moore(self, nums):
        majority_num = 0
        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num != num:
                count -= 1
            else:
                count += 1
        return majority_num

    # Bit manipulation
    # Pay attention: in python -2147483648 >> 31 = -1
    # Bit manipulation is somewhat different because of the python's syntax
    def majorityElement_bit(self, nums):
        bit_bucket = [0 for i in range(33)]
        for num in nums:
            bit_bucket[32] += (num >> 32) & 1
            for i in range(32):
                bit_bucket[i] += (abs(num) >> i) & 1

        majority_num = 0
        nums_len = len(nums)
        for i in range(32):
            if bit_bucket[i] > nums_len / 2:
                majority_num += 1 << i
        if bit_bucket[32] > nums_len / 2:
            majority_num *= -1
        return majority_num

    # two pass + dictionary
    def majorityElement1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums) // 2:
                return num

    # one pass + dictionary  # Hash table
    def majorityElement_hash(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            if dic[num] > (len(nums)/ 2):
                return num
            else:
                dic[num] += 1


    # TLE
    def majorityElement3(self, nums):
        for i in xrange(len(nums)):
            count = 0
            for j in xrange(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count > len(nums) // 2:
                return nums[i]

    # Sotring
    def majorityElement4(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    # Bit manipulation
    def majorityElement5(self, nums):
        bit = [0] * 32
        for num in nums:
            for j in xrange(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums) // 2:
                # if the 31th bit if 1,
                # it means it's a negative number
                if i == 31:
                    res = -((1 << 31) - res)
                else:
                    res |= 1 << i
        return res

    # Divide and Conquer
    def majorityElement6(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums) // 2]

    # the idea here is if a pair of elements from the
    # list is not the same, then delete both, the last
    # remaining element is the majority number
    def majorityElement7(self, nums):
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand


if __name__ == '__main__':
    nums = [1,2,2,2,3,5,4,4,4,4,2,4]
    s = Solution()
    print "\nMost frequent element is:",s.majorityElement(nums)
    print "\nMost frequent element is:",s.majorityElement_moore(nums)
    print "\nMost frequent element is:",s.majorityElement_hash(nums)
    print "\nMost frequent element is:",s.majorityElement_bit(nums)
