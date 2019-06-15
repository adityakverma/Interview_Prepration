
# Tags: Hash Table, Two pointer, String, AWS, Yelp, Adobe, Bloomberg
# Given a string, find the length of the longest substring without
# repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):

    def lengthOfLongestSubstring(self, s): #Aditya - Firstly - bad time complexity, as it uses two loops and secondly - it fails few test cases , like if input is "dvdf"
        if len(s) <= 0: return 0
        my_dict = {}
        max_count, count = 0, 0

        for i in range (len(s)):
            for j in range(i, len(s)):

                if s[j] not in my_dict:
                    my_dict[s[j]] = 1
                    count += 1
                    max_count = max(max_count,count)
                    #print s[j], count, max_count, my_dict.items()
                else:
                    count = 1
        return max_count

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)

    # -------------------------------------------------------------------------------------------
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
    def lengthOfLongestSubstring_(self, s):  # Aditya

        start = maxLength = 0 # start is updated to latest index, as soon as it finds char is repeated.
        usedChar = {}  # dictionary to keep track of latest char - index pair, based on occurance of char

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]: # meaning s[i] is being already considered in substring s[start, i] and it again appeared that s[i] is in usedChar - then update start, ELSE update max len
                start = usedChar[s[i]] + 1
                print "..",i, s[i],start
            else:
                maxLength = max(maxLength, i - start + 1) # We do +1 because loop starts from 0
                print "maxLength", i, start, maxLength, s[i]

            usedChar[s[i]] = i # Update value (i) of that char s[i].
            #print "Inserting %c : %d" %(s[i],usedChar[s[i]])
        return maxLength

    # In above : usedChar stores the last-seen position for a character,
    # usedChar[s[i]] >= start means s[i] is in the being considered substring s[start, i]
    # After we do start = usedChar[s[i]] + 1, there could be characters whose last seen
    # indexes stored in usedChar are from before start. We don't want to consider those characters as repeats because we are only considering the substring from start to i each iteration.

    # -------------------------------------------------------------------------------------------
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
    def lengthOfLongestSubstring1(self, s): # Same as above, but using enumerate

        start = maxLength = 0 # start is updated to latest index, as soon as it finds char is repeated.
        usedChar = {}  # dictionary to keep track of latest index of occurance of char
        for index, char in enumerate(s):
             if char in usedChar and start <= usedChar[char]:
                 start = usedChar[char] + 1
                 #print char, start
             else:
                maxLength = max(maxLength, index - start + 1)
             usedChar[char] = index
             #print usedChar.items(), maxLength
        return maxLength
    # -------------------------------------------------------------------------------------------


if __name__ == '__main__':
    string = "abcabcdabc"
    string1 = "dvdf"
    s = Solution()
    print "\nLongest Substring: ",s.lengthOfLongestSubstring(string)
    print "\nLongest Substring: ",s.lengthOfLongestSubstring_(string)
    print "\nLongest Substring: ",s.lengthOfLongestSubstring1(string)



# Need 3 temporary variables to find the longest substring: start, maxLength,
# and usedChars.
# Start by walking through string of characters, one at a time.
# Check if the current character is in the usedChars map, this would mean we
# have already seen it and have stored it's corresponding index.
# If it's in there and the start index is <= that index, update start
# to the last seen duplicate's index+1. This will put the start index at just
# past the current value's last seen duplicate. This allows us to have the
# longest possible substring that does not contain duplicates.
# If it's not in the usedChars map, we can calculate the longest substring
# seen so far. Just take the current index minus the start index. If that
# value is longer than maxLength, set maxLength to it.
# Finally, update the usedChars map to contain the current value that we just
# finished processing.
