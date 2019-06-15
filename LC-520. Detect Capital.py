
# Tags: Strings, Google
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
# Example 1:
#
# Input: "USA"
# Output: True
#
# Example 2:
#
# Input: "FlaG"
# Output: False

# Algorithm:
# If s[0] is Caps then two possibilities - Either remaining all can be caps or small for
# string to be valid. Else if s[0] is small then all should be small to be valid.


class Solution(object):     # ACCEPTED # Aditya's Solution
    def detectCapitalUse(self, s):

        if not s or len(s) <= 1:
            return True

        if ord(s[0]) in range(65, 91):   # IF First is capital, then two cases-
            if ord(s[1]) in range(65, 91): # Either all remaining are Capital starting from second letter.
                for i in range(2, len(s)):
                    if ord(s[i]) not in range(65, 91):  # Capital Letters
                        return False
            else:                          # Or all remaining are small letters starting from second letter.
                for i in range(2, len(s)):
                    if ord(s[i]) not in range(97, 123):  # Small letters
                        return False
        else:
            if ord(s[0]) in range(97, 123): # ELSE all must be small letters only
                for i in range(1, len(s)):
                    if ord(s[i]) not in range(97, 123):
                        return False
        return True

    #---------------------------------------------------

    def detectCapitalUse1(self, word):
        return word.isupper() or word.islower() or word.istitle()

    #---------------------------------------------------

    def detectCapitalUse2(self, word):

        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
        if word[0].islower():
            if word[1:].islower():
                return True

        return False

    #---------------------------------------------------
    def detectCapitalUse3(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if all(letter.islower() for letter in word):
            return True
        elif all(letter.isupper() for letter in word):
            return True
        elif word[0].isupper() and all(letter.islower() for letter in word[1:]):
            return True
        else:
            return False

    #---------------------------------------------------
    def detectCapitalUse4(self, word):
        import re
        #return True if re.match(r'[A-Z]+\Z|[A-Z]?[a-z]+\Z', word) else False  # \Z also indicates end of line
        #or
        return True if re.match(r'^[A-Z]+$|^[A-Z]?[a-z]+$', word) else False # ^ indiactes start, $ indicates end of line

    #---------------------------------------------------
    def detectCapitalUse5(self, word):
        return word.upper()==word or word[1:].lower()==word[1:]


if __name__ == '__main__':
    #str = "AdityaD"
    str = "aditya"
    s = Solution()
    print "\nDetect Capital:",s.detectCapitalUse(str)
    print "\nDetect Capital:", s.detectCapitalUse2(str)
    print "\nDetect Capital:", s.detectCapitalUse3(str)
    print "\nDetect Capital:", s.detectCapitalUse4(str)
    print "\nDetect Capital:", s.detectCapitalUse5(str)





