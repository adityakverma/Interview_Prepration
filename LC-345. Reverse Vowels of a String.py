
# Tags: Two Pointer, String, Google

# Write a function that takes a string as input and reverse only the vowels of a string.
# Example 1:
# Given s = "hello", return "holle".
# Example 2:
# Given s = "leetcode", return "leotcede".

class Solution(object):
    def reverseVowels_aditya(self, word): # 480/481 testcase passed on LC
        if word is None:
            return -1

        vlist = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowels = []
        index = []
        for i in range(len(word)):
            if word[i] in vlist:
                vowels.append(word[i])
                index.append(i)

        vowels = vowels[::-1]
        list1 = list(word)  # Note in string we cannot do assignments so we convert it to list
        for i, j in enumerate(index):
            list1[j] = vowels[i]
            word = ''.join(list1)
        return word

    def reverseVowels_Balaji(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(s) - 1
        s = list(s)
        while (start < end):
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            else:
                if s[start] not in vowels:
                    start += 1
                if s[end] not in vowels:
                    end -= 1
        return "".join(s)

    # Two-pointers
    def reverseVowels_TP(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vow = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        index = []
        word = []
        for i in range(len(s)):
            if s[i] in vow:
                index.append(i)
                word.append(s[i])
        for i in index:
            s[i] = word.pop()
            #print s
        return "".join(s)

if __name__ == '__main__':
    word = "leetcode"
    #word = 'aA'
    s = Solution()
    print "\nWord w/ reversed vowel is",s.reverseVowels_aditya(word)
    print "\nWord w/ reversed vowel is",s.reverseVowels_Balaji(word)



