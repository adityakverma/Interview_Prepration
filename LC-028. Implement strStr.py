# Tags: String, FB, Microsoft
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1: Input: haystack = "hello", needle = "ll"
# Output: 2

class Solution():

    def strStr_Balaji(self, haystack, needle):

        if not needle:  # Conner case-1
            return 0

        len1 = len(needle)
        len2 = len(haystack)
        if len1 > len2: # Conner case-2
            return -1
        elif len1 == len2:
            if needle == haystack:
                return 0
            return -1

        else:
            for i in range(len2-len1+1):
                if needle == haystack[i:i+len1]:
                    return i
        return -1

    def strStr(self, haystack, needle):
        if len(haystack) < len(needle): # early termination
            return -1
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


##################################################

if __name__ == '__main__':
    haystack = "hello"
    needle = 'll'
    s = Solution()
    print "\nIndex of substring is",s.strStr(haystack,needle)
    print "\nIndex of substring is",s.strStr_Balaji(haystack,needle)



#############################################

# https://leetcode.com/problems/implement-strstr/discuss/13237/Java-and-Python-solution-using-KMP-with-O(m-+-n)-time-complexity

# The time complexity for this solution should be O(m + n). First of all, we generate the "next" array to show any possible duplicates of prefix and postfix within needle. Then we go through haystack. Every time we see a bad match, move j to next[j] and keep i in current position; otherwise, move both of them to next position.
# Python solution using KMP with O(m + n) time complexity

def strStr(self, haystack, needle):
    if haystack == None or needle == None:
        return -1
    #generate next array, need O(n) time
    i, j, m, n = -1, 0, len(haystack), len(needle)
    next = [-1] * n
    while j < n - 1:
        #needle[k] stands for prefix, neelde[j] stands for postfix
        if i == -1 or needle[i] == needle[j]:
            i, j = i + 1, j + 1
            next[j] = i
        else:
            i = next[i]
        print i,j,next[i],next[j]
    #check through the haystack using next, need O(m) time
    i = j = 0
    while i < m and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            j = next[j]
    if j == n:
        return i - j
    return -1

