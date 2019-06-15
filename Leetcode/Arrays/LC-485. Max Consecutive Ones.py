
# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:

# Input: [1,1,0,1,1,1]
# Output: 3

class Solution():
    def findMaxConsecutiveOnes(self,arr):
        max_cnt = count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
                max_cnt = max(max_cnt, count)
            else:
                count = 0
        return max_cnt

if __name__ == '__main__':
    arr = [1,1,0,1,1,1]
    s = Solution()
    print "\nMax count for consecutive ones is: ",s.findMaxConsecutiveOnes(arr)
