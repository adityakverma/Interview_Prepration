

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#########################################################################################################

import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p) or not s or not p:
            return []

        need = collections.Counter(p)
        res = []
        l, r, missing = 0, 0, len(p)

        # print "need", need
        while r < len(s):  # Keep checking for all elements in given string 's'

            if need[s[
                r]] > 0:  # We found one element in S which we need (since need counter is >1), so reduce missing count
                missing -= 1

            need[s[r]] -= 1
            # print missing, r, s[r], need[s[r]]

            if missing == 0:  # If missing =0 meaning anagram ( rearranged letters) are found, then append result.
                res.append(l)  # Just append starting index as asked in question.

            if r - l == len(
                    p) - 1:  # If len of window (size of p) is same equal to r-l then we need to verify those elements & adjust missing
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1

            r += 1

        return res


'''
    Anagrams of p shares the same length as p
    -----------------------------------------
    Intuitively, for each plen-length substring in s, we check whether it is an anagram of p
    Time O(slen * plen * 26)

    To optimize:
    for current window (substring) [i, j),
    if it is not valid, we increase i by 1, and increase j by 1 // to make window length up to plen
    and check whether it is an anagram of p
    Time O(slen * 26)

    Try this example: "kjcbacbabacd"
                      "abc"
    Answer: [2,3,4,5,8]

'''

