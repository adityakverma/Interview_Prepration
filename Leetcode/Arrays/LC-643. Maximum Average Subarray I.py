
#  Given an array consisting of n integers, find the contiguous subarray of given length k
# that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

############################################################################################


class Solution():

    # My Solution
    def findMaxAverageSubArray(self,arr):
        max_avg = avg = float('-inf')
        for i in range(len(arr)):
            if i+3 <= len(arr)-1:
                avg = (arr[i]+arr[i+1]+arr[i+2]+arr[i+3])/float(4)
                max_avg = max(max_avg,avg)
        return max_avg

    # https://leetcode.com/problems/maximum-average-subarray-i/discuss/105469/Python-Straightforward-with-Explanation
    def findMaxAverage(self, A, K):
        su = 0
        ma = float('-inf')
        for i, x in enumerate(A):
            su += x
            if i >= K:
                su -= A[i - K]
            if i >= K - 1:
                ma = max(ma, su)
        return ma / float(K)


if __name__ == '__main__':
    arr = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    print "\nMax average subarray is:",s.findMaxAverageSubArray(arr)
    print "\nMax average subarray is:",s.findMaxAverage(arr,k)


# https://leetcode.com/problems/maximum-average-subarray-i/discuss/105469/Python-Straightforward-with-Explanation

