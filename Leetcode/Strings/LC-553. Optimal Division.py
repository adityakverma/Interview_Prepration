
# Tags: Math, String, Amazon

# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
#
# However, you can add any number of parenthesis at any position to change the priority of
# operations. You should find out how to add parenthesis to get the maximum result, and
# return the corresponding expression in string format. Your expression should NOT contain
# redundant parenthesis.

# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
# since they don't influence the operation priority. So you should return "1000/(100/10/2)".
#
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2

# TIP-1: [Aditya]
# This problem is a very tricky one. Basically the result is made of a product of some elements
# divided by the product of other elements. In the given example, we can see
# 1000/(100/10/2) == (1000*10*2)/(100). ==> This proofs we need to have second number as
# denominator, so lets start bracket from there.
#
# And one thing we shall notice is "NOTE 2. Elements in the given array will be in range
#  [2, 1000]." What does it mean? It means every element can contribute to a bigger results
#  as long as it's NOT in the denominator part! And we know no matter how we add parenthesis,
#  the second element must be in the denominator if it exist. And that's it!

# TIP-2
# # The key point of the problem is that we should get the largest numerator and the smallest
# # denominator. The only way to get the result is we always make the parenthesis begin from
# # the second number and end after the last number. Such as "1000/(100/10/2)" or
# # "1000/(2/200/10)".
# # After finding out the trick, we just need to operate with the strings.

# TIP-3
# Took me several minutes to verify this is correct since any reordering in denominator
# will increase the denominator for the result.

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums)) # Converting all int inputs in list to Str and putting in list
        #print nums
        if len(nums) > 2:
            nums[1] = "(" + nums[1]
            nums[-1] = nums[-1] + ")"
        return "/".join(nums)

if __name__ == '__main__':
    nums = [1000,100,10,2]

    s = Solution()
    print "\nOptimal Solution:", s.optimalDivision(nums)