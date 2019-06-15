
# Tags: Strings, Google
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k characters
# and left the other as original.
#
# Example: Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# https://leetcode.com/problems/reverse-string-ii/discuss/227799/Python-summary-of-three-methods:-1-two-pointer-2:-slicing-3-no-built-in-function
# ------------------------------------------------------------------

class Solution():

    #1. two pointer, interview favored
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            l, r = i, min(i + k - 1, len(s) - 1)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

    #2. Slicing
    def reverseStr__(self, s, k):
        res = ''
        for i in range(0, len(s), 2*k):
            res += s[i:i+k][::-1] + s[i+k:i+2*k]
        return res

    #3. USing inbuild function reverse()
    def reverseStr_(self, s, k):
        s = list(s)   # Important - Covert to list, so we can apply slicing. No Slicing can be applied on string directly too, but here we want to use revered function which works on lists only.

        for i in xrange(0, len(s), 2 * k):  # Important: steps is 2K, because question says: reverse every 2k characters counting from the start of the string.
            s[i:i + k] = reversed(s[i:i + k])
            #print i, s[i:i + k], s
        return "".join(s)  # In last convert list back to string.

if __name__ == "__main__":
    s = Solution()
    input = "abcdefg"
    k = 2
    print "\nReversed string:",s.reverseStr(input,k)



    # In Python, slices are handled safely with respect to indices that are out of bounds.

