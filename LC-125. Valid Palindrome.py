
# Tags, Two Pointer, String, Facebook, MS

# Given a string, determine if it is a palindrome, considering only alphanumeric 
# characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
# Input: "race a car"
# Output: false
import re

class Solution():

    # Two pointer approach - Aditya
    # Remove all special characters.
    # Convert to lower.
    # Join all words of sentence to one word - so we start comparing business
    def isPalindrome1(self,str):

        #print (str.strip(' '))
        string = re.findall(r'\w+', str.lower()) # Removes all punctiations and also converts to lower case
        print "....",string
        s = "".join(string); # print ",,,",s
        i, j = 0, len(s) - 1
        #print "Debug ",s, string, len(s), len(string)
        while i<j:
             if s[i] == s[j]:
                 i += 1
                 j -= 1
             else:
                 return False
        # for i in range(len(s)-1):
        #     if s[i] == s[len(s)-i]:
        #         continue
        #     else:
        #         return False

        return True

    def isPalindrome2(self, s):  # Balaji
        start = 0
        end = len(s) - 1

        while (start <= end):
            if not s[start].isalnum(): # isalnum() checks whether the string consists of alphanumeric characters.
                start += 1             # Here we're just trying to ignore white space and goto next alphabet which we can compare with other alphabet from end.
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
        return True

    def isPalindrome3(self, s):  # Balaji
        if not s:
            return True
        data = "".join([c.lower() if c.isalnum() else "" for c in s])
        if data[::-1] == data:
            return True
        return False

    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
         
if __name__ == '__main__':
    string = "A man, a plan, a canal: Panama"
    s = Solution()
    print "\nisPalindrome:",s.isPalindrome1(string)
    print "\nisPalindrome:",s.isPalindrome2(string)

# -------------------------
 # join vs split :

# input= 'This is a string, with words!'
# output = input.split(" ")
# print output # ['This', 'is', 'a', 'string,', 'with', 'words!']
#
# input = ['This', 'is', 'a', 'string,', 'with', 'words!']
# output = "".join(input) OR " ".join(newstr) # Depending on if u need space or not.
# print output # This is a string with words!

# ----------------------------

