

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

#######################################################################################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxlen = 0
        start = 0
        dt = {}

        # Algorithm: Basically If character is already seen then update start to new index - Its like moving left side of window.
        # Else if its new (then find maxlen & also add entry into hash) THEN window keeps getting bigger -right get updated later w/ for loop

        for i, c in enumerate(s):
            if c in dt:
                start = max(start, dt[c] + 1)

            maxlen = max(maxlen, i - start + 1)
            dt[c] = i
        return maxlen

###########################################################################################

'''

        start = maxLength = 0 # start is updated to latest index, as soon as it finds char is repeated.
        usedChar = {}  # dictionary to keep track of latest index of occurance of char

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]: 
                start = usedChar[s[i]] + 1

            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
'''


