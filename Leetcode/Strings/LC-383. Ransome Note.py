
# Given an arbitrary ransom note string and another string containing
# letters from all the magazines, write a function that will return true
# if the ransom note can be constructed from the magazines ; otherwise,
# it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

# In other words: find whether the letters in the note are a subset of those in the article, or whether the words themselves are a subset.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in ransomNote:
            # print ransomNote.count(c)
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True

        # ================================
        # if magazine is None or ransomNote is None:
        #     return False
        # ransomNote = sorted(ransomNote)
        # magazine = sorted(magazine)
        # print(magazine, ransomNote)
        #
        # for i in range(len(ransomNote)):
        #     if ransomNote[i] == magazine[i]:
        #         return True
        #     else:
        #         return False
        # =================================
        # if ransomNote in magazine:
        #     return True
        # return False

if __name__ == '__main__':
    ransomNote = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"
    #ransomNote = "a"
    #magazine = ""
    s = Solution()
    print "\nCan Construct:",s.canConstruct(ransomNote,magazine)


# The algorithm here is O(n^2) while the one using Counter is O(n).
# count is O(N). Thus, the total complexity should be O(N^2)?

# Using counter: I think the complexity is O(n) because a dictionary
# is used as a data structure, like a string aaa, and the dictionary
#  is like dict = {a:3} , so it takes O(1) to access the value .
# And the totally it is O(n)
