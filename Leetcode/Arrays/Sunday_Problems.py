
import collections

class Solution():

    # Accepted LC Solution
    def canPlaceFlowers_LC605(self, flowerbed, n): # All TC passes on LC. Accepted
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n

    # My Solution, but fails TC-05
    def CanPlaceFlowers(self, nums, n): # Works, but all test cases don't pass
        count = max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0

        if (max_count == (2*n + 1)) or ((nums[0] == 0 or nums[len(nums)-1] == 0) and max_count >= n):
            return True
        return False

    #####################################################################
    # My Solution. LC Accepted in first attempt.
    def largestNumAtleastTwice_LC747(self,nums):
        largest = max(nums)
        for i in range(len(nums)):
            if largest < 2*nums[i] and nums[i] != largest:
                return -1
        return nums.index(largest)

    def dominantIndex(self, nums):
        k = max(nums)
        x = nums.index(k)
        for i in range(len(nums)):
            if i == x:
                continue
            else:
                if nums[i]*2 > k:
                    return -1
        return x

    #####################################################################

    # Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
    # My Solution: Accepted in first attempt
    def thirdMaxNumber_LC414(self,nums):
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>= 3:
            return nums[2]
        return nums[0]

    # https://leetcode.com/problems/third-maximum-number/discuss/90227/Python-solution-use-set
    def thirdMax(self, nums):
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)

    #####################################################################

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

    #####################################################################
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103067/Python-O(N)-with-O(1)-space-complexity.-No-sorting
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/124333/Python-Sorting-and-Stack
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103075/python-unsorted-subarray

    def findUnsortedSubarray_LC581(self,nums):
        pass


    #####################################################################
    def maxConsecutiveOnes(self,nums):
        count = max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
        return max_count

    #############################################################
    # https://leetcode.com/problems/search-for-a-range/discuss/14869/Python-easy-solution-with-explanation
    # Using Binary Search with time complexity log(n)
    def searchRange_LC034(self, nums, target):

        start = 0
        end = len(nums) - 1
        result = []

        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        result.append(start)

        #-----------------
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        result.append(end)

        if result[0] > result[1]:
            return [-1, -1]
        else:
            return result

    # https://leetcode.com/problems/search-for-a-range/discuss/14706/Beats-100-Python-submission
    def searchRange(self, nums, target):
        n = len(nums)
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)/2
            if nums[m] < target: l = m+1
            else: r = m
        if nums[l] != target: return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)/2+1
            if nums[m] == target: l = m
            else: r = m-1
        right = l
        return [left, right]

    #############################################################
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/28128/Python-9-lines-2-extra-variables-76ms.-Any-simpler-solution-else

    def removeDuplicatesII_LC080(self, nums):
        if len(nums) < 3:
            return len(nums)
        pos = 1
        for i in range(1, len(nums)-1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1

    def removeDuplicates_LC026(self, nums):
        pos = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                nums[pos] = nums[i]
                pos += 1
        return pos

    #############################################################

    def SubarraySumWithK_LC560(self,nums):
        pass


if __name__ == '__main__':

    ###########################################################
    nums = [1, 0, 1, 1, 1, 0, 1, 1]
    s = Solution()
    print "\nMax consecutive one's:",s.maxConsecutiveOnes(nums)

    ############################################################
    flowerbed1 = [1, 0, 0, 0, 0, 0, 1] # TC-01
    flowerbed2 = [0, 0, 1, 0, 1]       # TC-02
    flowerbed3 = [1, 0, 0, 0, 1, 0, 0]
    flowerbed4 = [0, 0, 1, 0, 0]
    flowerbed5 = [1]
    n1 = 2
    n2 = 1
    n3 = 2
    n4 = 2
    n5 = 0
    #print "\nCan place flowers?",s.CanPlaceFlowers(flowerbed3,n3)
    print "\nCan place flowers?",s.canPlaceFlowers_LC605(flowerbed2,n2)

    ############################################################
    arr = [3, 6, 1, 0]
    print "\nLargest number atleast twice of others is at index:",s.largestNumAtleastTwice_LC747(arr)

    ############################################################

    myarr = [2, 2, 3, 1, 0]
    myarr1 = [4,3]
    print "\nThird Max number :",s.thirdMaxNumber_LC414(myarr1)

    #############################################################

    Input = [3, 1, 4, 1, 5]
    k = 2
    print "\nK-Diff Pairs in Array:",s.K_diffPairsinArray(Input,k)

    ###########################################################
    InputArr = [5,7,7,8,8,10]
    target = 8
    print "\nSearch Range:",s.searchRange_LC034(InputArr,target)
    print "Search Range:",s.searchRange(InputArr,target)

    ###########################################################
    array1 = [1,1,2,2,2,3,4,4,4,5]
    print "\nRemove dups from Sorted Array-II:",s.removeDuplicatesII_LC080(array1)
    array2 = [0,0,1,1,1,2,2,3,3,4]
    print "\nRemove dups from Sorted Array-I :",s.removeDuplicates_LC026(array2)

    ###########################################################

    ###########################################################