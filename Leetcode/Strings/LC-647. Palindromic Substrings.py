
# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different
# substrings even they consist of same characters.
#
# Example 1: Input: "abc" ,Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2: Input: "aaa", Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution(object):

    #################################################
    # https://leetcode.com/problems/palindromic-substrings/discuss/137002/Clear-Python:-DP-(Beat-23)-Two-Pointers-(Beat-77)-Manacher's-Algorithm-(Beat-100)
    # Two Pointers solution
    # Time Complexity = O(n^2)
    # Space Complexity = O(1)

    def countSubstrings2(self, s):

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        count = 0
        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i + 1)
        return count

    def helper(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[r] == s[l]:
            count += 1
            l -= 1
            r += 1
        return count




    def countSubstrings2_(self, s):

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        count = ""
        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i + 1)
        return count

    def helper_(self, s, l, r):
        while l >= 0 and r < len(s) and s[r] == s[l]:
            l -= 1
            r += 1
        print s[l:r+1]
        return s[l:r+1]
    ###################################################

    def countSubstrings3(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        res = 0
        for i in range(len(s)):
            res += (self.check(i, i, s) + self.check(i, i + 1, s))
        return res

    def check(self, x, y, s):
        count = 0
        while x >= 0 and y < len(s):
            if s[x] != s[y]:
                return count
            else:
                count += 1  # expanding outwards for every call to this function, and checking, so with all match we increment count.
            x -= 1
            y += 1
        return count

    #########################################################






















    # https://leetcode.com/problems/palindromic-substrings/discuss/140790/python-easy-solution

    def countSubstrings4(self, s):  # easiest
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        res = 1
        for i in range(1, len(s)):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    res += 1
        return res
    ######################################################

    def countSubstrings(self, s):  # My solution runs well for most inputs, but give TLE for submission.
        count = 0                  # Also time complexity is bad, so not great solution for interviews
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    start = i
                    end = j
                    while(start <= end):
                        if s[start] == s[end]:
                            if start == end or start == end-1:
                                count += 1
                            start += 1  # Moving inwards since start and end are two ends
                            end -= 1
                        else:
                            break
        return count+len(s)

if __name__ == '__main__':

    input = "aaa" #"fdsklf" #"aaa"
    s = Solution()
    print "\nPalindromic Substrings count:",s.countSubstrings(input)
    print "\nPalindromic2 Substrings count:",s.countSubstrings2(input) # <==
    print "\nPalindromic Substrings count:",s.countSubstrings3(input)
    print "\nPalindromic4 Substrings count:",s.countSubstrings4(input)  # <==