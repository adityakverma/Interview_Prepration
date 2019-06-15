
#  Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
#
# Example 1:
#
# Input: "aba"
# Output: True
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# ADITYA : This looks similar to LC-516 where we used Dynamic programming

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:      # If left and right not equal only then do below and check, else line 36
                one, two = s[left:right], s[left + 1:right + 1] # one becomes s[1:4] = bsb and two becomes s[2:5] = sbs
                #print one,two, left, right
                return one == one[::-1] or two == two[::-1] # This is actually like return isPalindrome(s, l+1, r) || isPalindrome(s, l, r-1);
            else:
                left, right = left + 1, right - 1 # If digits are equal then keep going and eventually return True
        return True

    def valid_Palindrome(self,s):
        # Base case
        if s is None:
            return True

        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l+1:r+1]
                return one == one[::-1] or two == two[::-1]
            else:
                l += 1
                r -= 1
        return True

# [ALGORITHM]:
# We can use the standard two-pointer approach that starts at the left and right
# of the string and move inwards. Whenever there is a mismatch, we can either
# exclude the character at the left or the right pointer. We then take the two
# remaining substrings and compare against its reversed and see if either one is a palindrome.

if __name__ == '__main__':
    s = Solution()
    input = "absbsa"
    print "\nValid Palindrome: ",s.validPalindrome(input)
    
    print "\nValid Palindrome: ",s.valid_Palindrome(input)




