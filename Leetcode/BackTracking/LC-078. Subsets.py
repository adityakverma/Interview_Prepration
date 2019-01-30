
# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).

# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
#
# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution():

    #################################################

    def LC078_Subsets(self,nums):
        res = []
        if len(nums) < 1:
            return 0
        self.backtrack_LC078(nums,0, [])

    def backtrack_LC078(self, nums, i, cur):
        print cur[:],  # No if condition, since we need all possibilities
        for c in range(i,len(nums)):
            cur.append(nums[c])
            self.backtrack_LC078(nums, c+1, cur) # IMP: change i+1 to c+1 to get correct answer. Else you get re-arrangement with dups.
            cur.pop()

    #################################################
    # LC-078: No dup inputs, hence there will be no question of dup subsets
    # Iteratively
    def subsets3(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

    def subsets_aditya_LC078(self, nums):
        nums.sort()  # This seem optional.. you will still get all subsets.
        result = [[]]
        for num in nums:
            #print "num", num
            result += [i + [num] for i in result]
            #print "result",result
        return result

    ################################################
    # LC-090: Dup inputs, so possibily there will be dup subsets, but we dont want dup sussets, so this solution

    def subsets_WithoutDupOutput_LC090(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            res += [ i + [num] for i in res if i + [num] not in res]
        return res

    def subsets_usingSets_LC090(self,nums):
        nums.sort()
        res = {()}
        for num in nums:
            res |= {r + (num,) for r in res}
        return list(res)

    #####################################################


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [1,2,2] # or num = ['A','B','C']
    s = Solution()

    print "\nLC-078, Subsets w/o dup inputs ",s.subsets_aditya_LC078(nums1)  # REGULAR : Without dups input. IF dups then sets might repeat. (Regular, solution)
    print "LC-078, Subsets w/ dup inputs  ",s.subsets_aditya_LC078(nums2)  # With dups input. But sets are also duplicated which we dont want as per LC-090

    #  Dup inputs but No duplicates sets ....
    print "\nSo as seen above, same function with dup inputs give duplicate sets, so we use new function as below"
    print "\nLC-090, Subsets w/ dup inputs, but no dup sets: ",s.subsets_WithoutDupOutput_LC090(nums2)  # Without Dups
    print "LC-090, Subsets w/ dup inputs, but no dup sets: ", s.subsets_usingSets_LC090(nums2)

