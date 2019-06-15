
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
#----------------------------------------------------------------


class Solution(object):

    def divide(self, dividend, divisor):

        positive = (dividend < 0) is (
                    divisor < 0)  # Its actually a XOR operation. It's for checking both dividend, divisor are +ve or -ve
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while dividend >= divisor:

            temp = divisor
            i = 1

            # subtract with (2* divisor), (4 * divisor) and so on from dividend until the dividend is smaller than the 2n * divisor
            while dividend >= temp:
                dividend -= temp
                res += i

                i <<= 1
                temp <<= 1

        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


# https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code?page=3
# https://www.youtube.com/watch?v=VKemv9u40gc

# [Aditya]: Just think how we used to divide in schools. See above youtube video if needed. Basically Inner while loop check whats max we can divide first digits. So we keep subrating dividend with temp and incrementing res, which gives we can use that res value for first time division. Once that is done we goto outer loop for remaining dividend.

'''
# It will make sure both dividend and divisor are positive or negative.
# i <<=1 is the same as i = i * 2, and temp <<= 1, is the same as temp *=2

The inner loop tries to subtract with (2* divisor), (4 * divisor) and so on from dividend until the dividend is smaller than the 2n * divisor. Once dividend is smaller than 2n*divisor, we set n = 1 and start again.

Let's take an example: 50 / 4
At the start,
temp, i = divisor, 1 # dividend = 50, temp = 4, i = 1
dividend -= temp # dividend = 46, temp = 4 , i = 1
res += i # res = 1
i <<= 1 # dividend = 46, temp = 4 , i = 2
temp <<= 1 # dividend = 46, temp = 8 , i = 2

Second iteration:
dividend -= temp # dividend = 38, temp = 8 , i = 2
res += i # res = 3
i <<= 1 # dividend = 38, temp = 8 , i = 3
temp <<= 1 # dividend = 38, temp = 12 , i = 3

and so on, when dividend > temp, we start over again with temp = 4, and i = 1

'''
