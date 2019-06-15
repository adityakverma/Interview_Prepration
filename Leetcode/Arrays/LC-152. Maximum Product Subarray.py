

class Solution():

    def maxProduct_SubArray(self, A):
        product = 1
        result = A[0]
        for i in range(len(A)):
            #print "CUR, A[i]", current, A[i]
            product *= A[i]
            result = max(product,result)
            #print "Current result ", (product, result)
            product = max(0,product)
        return result


if __name__ == '__main__':

    nums1 = [2,3,-2,4]
    nums = [-3,-4]
    s = Solution()
    print s.maxProduct_SubArray(nums)





