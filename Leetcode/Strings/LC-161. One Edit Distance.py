
# Given two strings s and t, determine if they are both one edit distance apart.

# Note:
#
# There are 3 possiblities to satisify one edit distance apart:
#
#     Insert a character into s to get t
#     Delete a character from s to get t
#     Replace a character of s to get t
#
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
#
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
#
# Example 3:
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
#
# =================================================================

# Check Article:  <============

# Only need functions for substitution and add/delete (based on the length of the strings)
# onemodify == substitution
# onedelete == add/delete

class Solution():

    def isOneEditDistance(self, s, t):
        s_len, t_len = len(s), len(t)
        if abs(s_len - t_len) > 1:
            return False
        if s_len == t_len:
            return self.onemodify(s, t)
        elif s_len > t_len:
            return self.onedelete(s, t)
        else:
            return self.onedelete(t, s)


    def onemodify(self, s, t):
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
        return diff == 1


    def onedelete(self, s, t):
        i, j = 0, 0
        while (i < len(s) and j < len(t)):
            if s[i] != t[j]:
                return s[i + 1:] == t[j:]
            i += 1
            j += 1
        return True
