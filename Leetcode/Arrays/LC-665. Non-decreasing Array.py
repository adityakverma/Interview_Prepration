
# Given an array with n integers, your task is to check if it could become non-decreasing by
# modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Well, I use count to remember how many descending pairs in the array, if count>=2, obviously we cannot modify a single element
# to obtain a non-descreaing array, so we return False.
#
# When count equals one, we check if we can modify nums[i] (the first one  in the descending pair, by decreasing it)
# or nums[i+1] (the second one in the descending pair, by increasing it), if in both
# situations, we cannot, then we will also return False. In this way, the situation that return False is complete, the others
# will return True. And also in this way, we can return much earlier :-)


class Solution():

    # https://leetcode.com/problems/non-decreasing-array/discuss/106842/The-easiest-python-solution....
    def checkPossibility(self, nums):
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i+2]<nums[i])):
                    return False
        return True


    def findNonDecreasingArray_Aditya(self,arr):  # Does work for all testcases. PASS on LC, but doesn't submits.
        if len(arr) <= 1: return True
        flag = 1
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                if flag:
                    arr[i] = arr[i + 1] - 1
                    flag = 0
                else:
                    return False
        return True

if __name__ == '__main__':
    arr = [4,2,3]
    arr1 = [3,4,2,3]
    arr2 = [-1,4,2,3]

    s = Solution()
    print "\nCan we convert to non-decreasing array ?",s.findNonDecreasingArray_Aditya(arr)
    print "\ncheckPossibility ?", s.checkPossibility(arr2)