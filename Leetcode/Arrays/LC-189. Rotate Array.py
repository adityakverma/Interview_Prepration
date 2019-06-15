
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]

# Note:
#     Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?

class Solution():

    # In-place solution using slicing
    def rotateArray_Right(self, nums, k):  # LC Accepted
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]
        return nums

    def rotateArray_Left(self, nums, k):
        nums[:] = nums[k:] + nums[:k]
        return nums

    # -----------------------------------
    def rotateArrayLeft_(self,arr, n, d):
        for i in range(0, d):
            self.rotateArrayByOne(arr, n)
        return arr

    def rotateArrayByOne(self, arr, n):
        temp = arr[0]
        for i in range(0, n - 1):
            arr[i] = arr[i + 1]
        arr[i + 1] = temp
    # ------------------------------------

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    k = 2
    s = Solution()
    print "\nOriginal Array     :", arr
    print "Rotated Array Left :", s.rotateArray_Left(arr, k)
    #print "Rotated Array Left :", s.rotateArrayLeft(arr, len(arr),k)

    arr = [1, 2, 3, 4, 5, 6, 7]
    print "\nOriginal Array     :", arr
    print "Rotated Array Right:",s.rotateArray_Right(arr,k)


# python sub-indexing create a copy of the range specified, so I believe the space complexity on this one is O(n)
# Space Complexity : O(n) as we do sub-indexing
# Time Complexity  : O(1)


