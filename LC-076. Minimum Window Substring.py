
# Tags: Hash, two pinter, Strings, Facebook, Uber, LinkedIn
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
# Note:
#     If there is no such window in S that covers all characters in T, return the empty string "".
#     If there is such window, you are guaranteed that there will always be only one unique minimum window in S


# ---------------------------------------------------------------------------------
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i, j = 0, 0
        n = len(s)
        res = "#"
        miss = len(set(t))

        freq = collections.Counter(t)
        sofar = collections.defaultdict(int)

        print freq, sofar

        while j < n:
            if miss and s[j] in freq:  # miss tells how many characters of target are still missing in S. Id miss=0 window found.
                sofar[s[j]] += 1
                if sofar[s[j]] == freq[s[j]]:
                    miss -= 1
            j += 1
            while i <= j and not miss:  # If miss=0 from above 'if' block that whole target has been found in that window
                if res == "#" or len(res) > len(s[i:j]):
                    res = s[i:j]  # Ensuring we have minimum window, which contains all elements of target.

                if s[i] in freq:  # Also if nothing is missing, remove as much as possible from window start and update result
                    sofar[s[i]] -= 1  # This is like moving the window

                    if sofar[s[i]] == freq[
                        s[i]] - 1:  # But if while reducing window, we loose target element itself, then increment miss
                        miss += 1
                i += 1

        return "" if res == "#" else res


# # https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59110/O(N)-template-for-Minimum-Size-Subarray-Sum-and-Minimum-Window-Substring-and-Longest-Substring-Without-Repeating-Characters

'''
#  The algorithm has two major phases.
#     Find the first window that contains all letters in t;
#     Keep expanding the window to the right by 1 char at a time, reducing left side if possible.

#     The best part is to make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
#     In this case, every time the window is expanded, only the new char need to be checked.
'''

# ---------------------------------------------------------------------------------

class Solution_(object):
    def minWindow(self, s, t):  # Balaji & also https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python

        print s, t
        import collections
        need, missing = collections.Counter(t), len(t)
        print "\nneed, missing",need, missing
        i = I = J = 0

        for j, c in enumerate(s, 1):
            print "\nj c ...",j, c
            if need[c] > 0:
                missing -= 1
                print "if __", need[c], missing

            need[c] -= 1
            print "c, need[c] ...", c,need[c]

            if not missing:
                print "||| Inside if - missing:", missing
                print i, j, s[i], need[s[i]]
                while i < j and need[s[i]] < 0:
                    print "WHILE", s[i], need[s[i]]
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

if __name__ == '__main__':

    S = "ADOBECODEBANC"
    T = "ABC"

    s = Solution()
    s.minWindow(S, T)
    #print "\nMin window:",s.minWindow(S,T)

# Last Edit: July 11, 2018 4:13 PM
# StefanPochmann
# StefanPochmann
#  22848
#
# The current window is s[i:j] and the result window is s[I:J]. In need[c] I
# store how many times I need character c (can be negative) and missing tells
# how many characters are still missing. In the loop, first add the new
# character to the window. Then, if nothing is missing, remove as much as
# possible from the window start and then update the result.
#
# def minWindow(self, s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]

#  The algorithm has two major phases.
#     Find the first window that contains all letters in t;
#     Keep expanding the window to the right by 1 char at a time, reducing left side if possible.

#     The best part is to make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
#     In this case, every time the window is expanded, only the new char need to be checked.

# ---------------------------------------------------------------------------------


