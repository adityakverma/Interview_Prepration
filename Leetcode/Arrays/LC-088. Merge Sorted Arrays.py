
# Tags: Array, Two-Pointers, FB, MS
# =================================

class Solution(object):

    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            #print m,n
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:   # Special case when m=0 and n=1 as inputs
            nums1[:n] = nums2[:n]
        print "\nMerged Array Result :", nums1


if __name__ == '__main__':

    nums1 = [1, 7, 9, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 4]
    m = 3
    n = 4

    num1 = [0]
    num2 = [1]
    m1 = 0
    n1 = 1


    s = Solution()
    s.merge(nums1,m,nums2,n)
    s.merge(num1,m1,num2,n1)


# Other Solution:
#     nums1[m:]=nums2
#     nums1.sort()