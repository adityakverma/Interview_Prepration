
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# This problem is pretty much equivalent to Isomorphic Strings.
# Let me reuse two old solutions.
# https://leetcode.com/problems/word-pattern/discuss/73433/Short-in-Python


class Solution():
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        print s, t, map(s.find,s), map(t.index,t)
        return map(s.find, s) == map(t.index, t)

    def wordPattern2(self, pattern, str):
        d = dict()
        words = str.split(" ")

        l1 = len(pattern)
        l2 = len(words)

        if l1 != l2:
            return False

        for p in xrange(l1):  # iterate through items in words and pattern

            if pattern[p] in d.keys():  # check if the pattern exists and the word match the value

                if d[pattern[p]] != words[p]:
                    return False
            else:

                if words[p] in d.values():  # if the pattern not exists, but the value exists return False
                    return False

            d[pattern[p]] = words[p]  # if both the pattern and value not exist, add to dictionary

        return True

pattern = "abba"
str = "dog cat cat dog"

s = Solution()
print s.wordPattern(pattern,str)

'''
    wordList = str.split()
    n1 = len(pattern)
    n2 = len(wordList)
    if (n1 != n2):
        return False
    else:
        wordList = str.split()
        # wordList = [s.encode('ascii') for s in wordList]
        # pattern = [s.encode('ascii') for s in pattern]
        mydict = {}
        result = True
        for i in range(len(pattern)):
            if (pattern[i] not in mydict):
                if wordList[i] not in mydict.values():
                    mydict[pattern[i]] = wordList[i]
                else:
                    result = False
                    break
            else:
                if (mydict[pattern[i]] != wordList[i]):
                    result = False
                    break
        return result
        
'''


