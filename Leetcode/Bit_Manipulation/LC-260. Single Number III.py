
# Once again, we need to use XOR to solve this problem. But this time, we need to do it in two passes:
#
#     In the first pass, we XOR all elements in the array, and get the XOR of the two numbers we need to find. Note that since the two numbers are distinct, so there must be a set bit (that is, the bit with value '1') in the XOR result. Find
#     out an arbitrary set bit (for example, the rightmost set bit).
#
#     In the second pass, we divide all numbers into two groups, one with the aforementioned bit set, another with the aforementinoed bit unset. Two different numbers we need to find must fall into thte two distrinct groups. XOR numbers in each group, we can find a number in either group.
#
# Complexity:
#
#     Time: O (n)
#
#     Space: O (1)

# Finally understand it.
#
#     Let a and b be the two unique numbers
#     XORing all numbers gets you (a xor b)
#     (a xor b) must be non-zero otherwise they are equal
#     If bit_i in (a xor b) is 1, bit_i at a and b are different.
#     Find bit_i using the low bit formula m & -m
#     Partition the numbers into two groups: one group with bit_i == 1 and the other group with bit_i == 0.
#     a is in one group and b is in the other.
#     a is the only single number in its group.
#     b is also the only single number in its group.
#     XORing all numbers in a's group to get a
#     XORing all numbers in b's group to get b
#     Alternatively, XOR (a xor b) with a gets you b.

# https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C++Java-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations?page=2

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        xor = xor & (xor - 1) ^ xor

        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]



# ---------------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/single-number-iii/discuss/68943/Examples-to-explain-the-XOR-solution-and-bit-manipulation-trick
# Examples to explain the XOR solution and bit manipulation trick

# The concrete solution and explanation are showed on the most voted answers,now I wanna make an example to help to understand the trick more easily.
# Assume we have the following array:
#
#     0010
#     0010
#     0110
#     0110
#     0100
#     0001
#
# We can see the last two numbers are unique,how can we find them?When we XOR all the numbers,it's the same as the result of XORing the last two numbers because duplicate numbers get zero in XOR operation.
# Here we get 0101(stored in variable diff),which means we have two bit difference between number 0100 and 0001 at 1st and 3rd bit. So we can simply distinguish them by any bit difference.
#
# The trick here is
#
# diff &=-diff
#
# or more human-readable
#
# diff &=~(diff-1)
#
# The codes above both have the same aim:get the rightmost bit 1 of the variable diff. Detail reference:Bit Manipulation
# As we know,every bit of 1 of variable diff can distinguish the two unique numbers,here we simply choose the rightmost 1 to divide all the numbers into two groups:
#
#     0010
#     0010
#     0110
#     0110
#     0100
#
# and
#
#     0001
#
# Now the problem has been converted to two simpler subproblem: Single Number
# XOR the two group respectively and we get the result.
#
# What if we use the leftmost bit 1 for division?We will get the following groups
#
#     0010
#     0010
#     0001
#
# and
#
#     0110
#     0110
#     0100
#
# Also we succeed to put the two unique numbers into two difference groups,so the problem is solved.
