
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs
# in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both
# numbers in the array and their absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
#
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
#
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

import collections
class Solution():

    def K_diffPairsinArray1(self,nums,k):
        #x = set()  # Note: If I just use list here it gives dup pairs since 1 is repeated - [(3, 5), (1, 3), (1, 3)]
        count = 0
        for i in nums:
            for j in nums:
                if j-i == k:
                    #x.add((i,j))
                    count += 1
        #return list(x)
        return count

    def K_diffPairsinArray(self, nums, k): # Got it
        res = 0
        c = collections.Counter(nums)
        #print c
        for i in c:
            #print i
            if ((k > 0 and i + k in c) or (k == 0 and c[i] > 1)):
                res += 1
        return res

    # https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100130/python-solution-with-comments-O(n)-time-with-90-use-only-one-set-for-most-of-cases
    def K_diffPairsinArray2(self, nums, k):

        if k < 0:
            return 0

        # the zero set defined only when k is 0 that mark the same number only count once
        zero = set()

        # add visited number in set for further comparison
        visited = set()
        cnt = 0
        for number in nums:
            if k != 0:
                if number not in visited:
                    if number + k in visited:
                        cnt += 1
                    if number - k in visited:
                        cnt += 1
                    visited.add(number)
            else:
                if number in visited and number not in zero:
                    cnt += 1
                    zero.add(number)
                else:
                    visited.add(number)
        return cnt


if __name__ == '__main__':

    s = Solution()
    Input = [3, 1, 4, 1, 5]
    k = 2
    print "\nK-Diff Pairs in Array:",s.K_diffPairsinArray(Input,k)
