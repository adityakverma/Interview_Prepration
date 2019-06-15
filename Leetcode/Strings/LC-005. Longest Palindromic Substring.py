
# Tags: Strings, DP, MS, AWS, Bloomberg
# Given a string s, find the longest palindromic substring in s. You may assume that
#  the maximum length of s is 1000.
#
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# Input: "cbbd"
# Output: "bb"

class Solution():
    # https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
    # https://leetcode.com/problems/longest-palindromic-substring/discuss/172203/Python-Simple-Solution-O(n2)-time-and-O(1)-space

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):

            # odd case, when result is like "aba"
            tmp = self.expand(s, i, i)
            #print "\ni ...", i,"tmp",tmp,"res", res
            if len(tmp) > len(res):
                res = tmp
                #print "even",res

            # even case, when result is like "abba"
            tmp = self.expand(s, i, i + 1)
            #print "i+1 ...", "tmp",tmp,"res", res
            if len(tmp) > len(res):
                res = tmp
                #print "odd", res
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r] # We do l+1 because before we had exit while we had done l -= 1 and right index is already one less in slicing

    def LC_516_longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] # 2 + look diagonally left down which is row+1 and col-1. Note [0][0] is on left top.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) # if s[i] != s[j] then its either of inner groups which are already pre-computed.

        return dp[0][n - 1]

    # https://leetcode.com/problems/longest-palindromic-substring/discuss/177196/Python-dp-and-Manacher's-Algorithm
    def longestPalindrom_DP(self, s):
        n = len(s)
        table = [[False for x in range(n)] for y in range(n)]

        start = -1
        max_len = 0
        for i in range(n, -1, -1):
            for j in range(i, n):
                if (i + 1 > j - 1 or table[i + 1][j - 1] == True) and s[i] == s[j]:
                    table[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        start = i

        return s[start:start + max_len]

# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
# https://leetcode.com/problems/longest-palindromic-substring/discuss/134306/python-O(n2)-solution
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2927/Simple-Python-Solution

# https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
# https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution



if __name__ == '__main__':
    arr = "babbabd"
    s = Solution()
    print "\nGiven String is:",arr
    #print "Longest Palindrome substring",s.longestPalindromeSubstring(arr)
    print "Longest Palindrome substring: ",s.longestPalindrome(arr)
    print "Longest Palindrome substring: ",s.longestPalindrom_DP(arr)
    print "Longest Palindrome substring length: ", s.LC_516_longestPalindromeSubseq(arr)

# I've added two condition which makes this a lot faster.:

# #check beforehand if the passed string is already a palindrome in itself
# #or if length of string is less than 3, then return s itself
# if (s==s[::-1] or len(s) < 3):
#     return s
#
# #check if "i" has crossed middle element and if length of largest
# #palindrome till found, is greater than half of total length of string
# #then break, we've found the answer no need to iterate more
# if (i>(leng//2) and len(ans)>(leng//2)):
#     break
#
# These two conditions surprisingly decreased the time from 1683ms(without these 2 conditions) to 323 ms(with the conditions). below is the full modified code.
#
# def longestPalindrome(self, s):
#     #check beforehand if the passed string is already a palindrome in itself
#     #or if length of string is less than 3, then return s itself
#     if (s==s[::-1] or len(s) < 3):
#         return s
#     res = ""
#     for i in xrange(len(s)):
#         # odd case, like "aba"
#         tmp = self.helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = self.helper(s, i, i+1)
#         if len(tmp) > len(res):
#             res = tmp
#         #check if "i" has crossed middle element and if length of largest
#         #palindrome till found, is greater than half of total length of string
#         #then break, we've found the answer no need to iterate more
#         if (i>(leng//2) and len(ans)>(leng//2)):
#             break
#     return res
#
# # get the longest palindrome, l, r are the middle indexes
# # from inner to outer
# def helper(self, s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1; r += 1
#     return s[l+1:r]


# -----------------------------------------------------------------
# My Solution, which doesn't work though well

#     def longestPalindromeSubstring(self,arr):
#         s = " "
#         print "Within"
#         for i in range(len(arr)):
#             for j in range(len(arr)-1,i+1,-1):
#                 print i,j
#                 print "arr[i] %s, arr[j] %s" %(arr[i],arr[j])
#                 if arr[i] == arr[j]:
#                     print "Equal", arr[i], arr[j]
#                     start = arr[i]
#                     end = arr[j]
#                     if s == " ":
#                          s = start + end




