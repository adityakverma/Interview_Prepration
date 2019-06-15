
# Tags: String, MS, Apple, Bloomberg
# Given an input string, reverse the string word by word.
#
# Example:
#
# Input: "the sky is blue",
# Output: "blue is sky the".

class Solution():

    # Time Complexity is O(n) ??
    def reverseWords(self, s):       # Aditya - Good one. First split words and reverse the order of words and just join them to make sting from list
        s = s.split()     #This will split the sentence in list of words.
        s = s[::-1]       #This will reverse the list. Time Complexity O(n)
        s = " ".join(s)   #This will join the list
        return s

    def reverseWords1(self, s):    # Interviewer wont like one line solution
        return ' '.join(s.split()[::-1])

    def Revisited_10_09_18(selfself,s):   #  <============= Good but LC dosesn't accept :(
        str = s.split(" ")
        return " ".join(str[::-1])

    #--------------------------------------------------
    def reverseWordsInString(self, s):  # My Solution
        r = m  = t = " "
        #s = s.split()
        r = s[::-1]
        for i in range(4):
            t = r.split()[i]
            m += t[::-1] + " "
        return m

if __name__ == '__main__':
    input = "the sky is blue"
    s = Solution()
    print"\nReversed word is:", s.reverseWordsInString(input)
    print"\nReversed word is:", s.reverseWords(input)
    print"\nReversed word is:", s.reverseWords1(input)
    print"\n10-9-18 Reversed word is:", s.Revisited_10_09_18(input)



