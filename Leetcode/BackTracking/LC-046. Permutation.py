# https://leetcode.com/problems/permutations/description/
# https://leetcode.com/problems/permutations/discuss/18378/Simple-python-code-without-recursion

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# ---------------------------------------------------------------------------------

class Solution():

    def LC046_Permutation(self, s):  # CORRECT SOLUTION
        if s is None:  # Boundry condition
            return 0

        res = []
        self.backtrack_LC046(s, 0, res)
        return res


    def backtrack_LC046(self, s, start, res):
        if start == len(s):
            print s[:]
            # res.append(s[:])
            return
        for x in range(start, len(s)):
            s[start], s[x] = s[x], s[start]  # Choose
            self.backtrack_LC046(s, start + 1, res)
            s[start], s[x] = s[x], s[start]  # Un-choose

'''        
class Solution_(object):

    def permute_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


        """
        def swap(i, j, nums):
            new_nums = list(nums)
            new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
            #print "swapped", new_nums
            return new_nums

        result = [nums,]

        for i in range(len(nums)-1):  # i=0,1
            #print "\ni ...... ",i, result[:]
            for one in result[:]:
                #print "\none",one,"....", result[:]
                for j in range(i+1, len(nums)):
                    #print "i,j,one :",i,j,one
                    result.append(swap(i, j, one))
        return result

    #######################################################
    def permute_2(self, nums):

        if not nums:
            return None

        result = [nums]
        for i in range(len(nums) - 1):
            for one in result[:]:
                for j in range(i + 1, len(nums)):
                    #print one[:i], one[j:], one[i:j]
                    result.append(one[:i] + one[j:] + one[i:j])
                    #print result
        return result
'''

if __name__ == '__main__':
    num = [1,2,3]
    str = ['A','B','C']
    s = Solution()
    print s.LC046_Permutation(str)

    #print num, num[:]
    #print s.permute_1(str)
    #print s.permute_2(str)

# --------------------------------------------------------
# i  0 [[1, 2, 3]]
#
# one [1, 2, 3] .... [[1, 2, 3]]
# i,j,one : 0 1 [1, 2, 3]
# swapped [2, 1, 3]
# i,j,one : 0 2 [1, 2, 3]
# swapped [3, 2, 1]
#
# i  1 [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
#
# one [1, 2, 3] .... [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
# i,j,one : 1 2 [1, 2, 3]
# swapped [1, 3, 2]
#
# one [2, 1, 3] .... [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 3, 2]]
# i,j,one : 1 2 [2, 1, 3]
# swapped [2, 3, 1]
#
# one [3, 2, 1] .... [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1]]
# i,j,one : 1 2 [3, 2, 1]
# swapped [3, 1, 2]
# [[1, 2, 3], [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1], [3, 1, 2]]


# ===========
# >>> a = [0]
# >>> b = a
# >>> a[:] = [1]
# >>> print(b)
# [1]                 <--- note, change reflected by a and b
# >>> a = [2]
# >>> print(b)
# [1]                 <--- but now a points at something else, so no change to b