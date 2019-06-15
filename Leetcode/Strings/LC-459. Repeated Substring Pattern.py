
# Using KMP Algo:

# Given a non-empty string check if it can be constructed by taking a substring of it and
# appending multiple copies of the substring together. You may assume the given string consists
# of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# ============================================================================================

class Solution(object):
    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94393/Python-KMP-O(n)
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        # ----------------------------------------------------------------------------
        # Compute temporary array to maintain size of suffix which is same as prefix
        # Time/space complexity is O(size of pattern)

        def computeLPS(str):  # lps indicates longest proper prefix which is also suffix
            lps = [0] * len(str)

            i = 1
            j = 0
            while i < len(str):
                if str[i] == str[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps            # This array lps, will help us in doing substring search. Time Complexity of this O(n) & space complexity is also O(n)
                                  # Next: Lets apply this substring search ( pattern) to real string (text) to find, if that pattern exists in that text. See the KMP function below in java.  Note LC-76 is different, to find min window, where char may not be continous
        # -------------------------------------------------------------------------------

        lps = computeLPS(str)
        print "\nlps array:",lps

        n = len(str)
        lenn = lps[-1]
        if lenn and n % lenn == 0:  # OR if lenn and n % (n - lenn) == 0:   # Most important or tweek to get this solution via KMP algo.
            return True
        else:
            return False

        # For example, "bcabca" = [0,0,0,1,2,3] and "bcabc" = [0,0,0,1,2]
        # Now, if length of string is N, and we find LPS[-1] = L,
        # IMP: In order to check if the string is periodic, that is string is obtained by repeated substrings,
        # we need to check, N>0 and N%(N-L) == 0.

if __name__ == '__main__':
    A = 'abcabc'
    s = Solution()
    print "\nDo we have repeated substring:",s.repeatedSubstringPattern(A)

# Must See this KMP algorithm video for pattern search:
# https://www.youtube.com/watch?v=GTJr8OvyEVQ [ time 5:33 - 10:18 ] - for this problem
# His equivalent Java code: https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java
# Python code too: https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/




