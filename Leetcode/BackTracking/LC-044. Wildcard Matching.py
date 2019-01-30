#
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#

# The main function that checks if two given strings match.
# The first string may contain wildcard characters

class Solution():

    # A function to run test cases
    def test(self, first, second):
        if self.match(first, second):
            print "Yes"
        else:
            print "No"

    # first string contains wildcard. second string is regular string.
    def match(self,first, second):
        # If we reach at the end of both strings, we are done
        if len(first) == 0 and len(second) == 0:
            return True

        # Make sure that the characters after '*' are present
        # in second string. This function assumes that the first
        # string will not contain two consecutive '*'
        if len(first) > 1 and first[0] == '*' and len(second) == 0:
            return False


        # NOW If the first string contains '?', or current characters
        # of both strings match
        if (len(first) > 1 and first[0] == '?') or \
                (len(first) != 0 and len(second) != 0 and first[0] == second[0]):
                return self.match(first[1:], second[1:])

        # NOW If there is *, then there are two possibilities because
        # '*' Matches any sequence of characters (including the empty sequence).
        # a) We consider current character of second string [ accept any sequence ]
        # b) We ignore current character of second string.  [ empty sequence ]
        if len(first) != 0 and first[0] == '*':
            return self.match(first[1:], second) or \
                   self.match(first, second[1:])            # empty sequence

        return False



if __name__ == "__main__":

    s = Solution()

    # Driver program
    s.test("g*ks", "geeks")  # Yes
    s.test("ge?ks*", "geeksforgeeks")  # Yes
    s.test("g*k", "gee")  # No because 'k' is not in second
    s.test("*pqrs", "pqrst")  # No because 't' is not in first
    s.test("abc*bcd", "abcdhghgbcd")  # Yes
    s.test("abc*c?d", "abcd")  # No because second must have 2 instances of 'c'
    s.test("*c*d", "abcd")  # Yes
    s.test("*?c*d", "abcd")  # Yes

# Why do we use slicing? This takes exponential memory to create new strings and
# copy every time We can just use indices as follows (this will save space):
# https://leetcode.com/problems/regular-expression-matching/discuss/5678/Fast-Python-solution-with-backtracking-and-caching-+-DP-solution


