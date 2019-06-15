
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/139503/Python-solution-using-2-pointers-to-shrink-the-range
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).


class Solution():

    # two-pointer # we moved the pointers from two ends toward the middle, we actually abandoned those visited nodes.
    def twoSum_TP(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    def two_sum_TP(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while (j != i):
            if (numbers[j] + numbers[i] > target):
                j -= 1
            if (numbers[i] + numbers[j] < target):
                i += 1
            if (numbers[i] + numbers[j] == target):
                break
        return [i + 1, j + 1]

    # dictionary
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i


    # binary search
    def twoSum_BS(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

if __name__ == '__main__':

    numbers = [2,7,11,15]
    target = 9
    s = Solution()
    print "\nTwo Pointer Solution-1 :", s.twoSum_TP(numbers,target)
    print "\nTwo Pointer Solution-2 :", s.two_sum_TP(numbers, target)
    print "\nBinary Search Solution :", s.twoSum_BS(numbers, target)

