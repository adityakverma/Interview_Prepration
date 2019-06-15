
# Tag: Array, Math, Facebook

#  Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.

class Solution():
    def MaxSwap(self,num):

        swapped = ""
        s = list(str(num))
        max_index = s.index(max(s))
        if max_index != 0:
            s[0],s[max_index] = s[max_index],s[0]
        #for i in s:
        #    swapped += str(i)
        #return int(swapped)
        return int("".join(s))

    # Good Solution. Please understand this... its easy
    def maximumSwap(self, num):
        A = list(str(num))
        ans = A[:]
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                A[i], A[j] = A[j], A[i]
                #print A
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))


if __name__ == '__main__':
    num = 2736
    num1 = 98368 # Output 98863
    s = Solution()
    print "\nMax Swap: ",s.MaxSwap(num)
    print "\nMax Swap: ",s.maximumSwap(num1)


# It's pretty simple really:
#
# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array
#
# There is also the step value, which can be used with any of the above:
#
# a[start:end:step] # start through not past end, by step
