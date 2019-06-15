

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8


class Solution(object):

    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)
        #return sum(range(min(nums), (min(nums)+len(nums)+1))) - sum(nums)     # Works perfect if sequence is [4,5,6,8]

    def missingNumber2(self, nums):
        n = len(nums)
        return ( (n * (n + 1)) / 2) - sum(nums)  # Sum of n natural numbers is [n * (n+1)/2]


if __name__ == '__main__':

    nums = [9,6,4,2,3,5,7,0,1]
    #nums = [4,5,6,8]  # Here answer is -13, which is wrong. However, I think in the question it says the sequence starts with a 0. If 0 is missing then, the array must definitely start with a 1.
    s = Solution()

    print "\nMissing Number is: ", s.missingNumber(nums)
    print "\nMissing Number is: ", s.missingNumber2(nums)

    # Time Complexity: O(n) as sum will have time complexity of O(n)


    # 41. First Missing Positive

    