
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist,
# return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.
#
# Example 2:
# Input: [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#
# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


class Solution():

    # Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
    # My Solution: Accepted in first attempt
    def thirdMaxNumber_LC414(self,nums):
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>= 3:
            return nums[2]
        return nums[0]

    # https://leetcode.com/problems/third-maximum-number/discuss/90227/Python-solution-use-set
    def thirdMax(self, nums):
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)

if __name__ == '__main__':

    s = Solution()
    myarr = [2, 2, 3, 1, 0]
    myarr1 = [4,3]
    print "\nThird Max number :",s.thirdMaxNumber_LC414(myarr)