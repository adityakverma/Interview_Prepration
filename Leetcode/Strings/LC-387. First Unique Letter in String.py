
# Tags: Hash, String, Google, AWS, MS

#  Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

class Solution():
    def uniqueLetter_aditya(self,s):  # ACCEPTED

        if len(s) == 1:
            return 0
        if len(s) < 1:
            return -1

        for i in range(len(s)-1):  # Note since we are checking for occurance of string in s[i+1:] so we take range as (len(s)-1)
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i

        if s[-1] not in s[:-1]:  # Special case
            return len(s)-1
        return -1

    def firstUniqChar_Balaji(self, s):
        dic = {}
        for c in s:
            if c in dic:  # OR  if c in tdict.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        for index, c in enumerate(s):
            if dic[c] == 1:
                return index
        return -1

    def firstUniqChar(self, s): # TLE .. Not accepted
         for i in range(len(s)):
            if s.count(s[i])==1:
                return i
         return -1

if __name__ == '__main__':
    s = Solution()
    word1 = "loveleetcode"
    word2 = "aadadaad"       # Answer is 6 and it should be  -1
    word = "dddccdbba"
    print "\nFirst unique letter is at index",s.uniqueLetter_aditya(word)
    print "\nFirst unique letter is at index",s.firstUniqChar_Balaji(word)
    print "\nFirst unique letter is at index",s.firstUniqChar(word)

