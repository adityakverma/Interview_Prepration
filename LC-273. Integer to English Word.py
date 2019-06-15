
# Tags: Math, String, Facebook, MS
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1: Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:  Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3: Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# https://leetcode.com/problems/integer-to-english-words/discuss/111644/Clean-python-recursion-beat-97
class Solution(object):

    def numberToWords(self, num):

        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                     "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        if num == 0:
            return "Zero"
        ret = ""
        if num / 1000000000 != 0:
            ret += self.numberToWords(num / 1000000000) + " Billion "
            num %= 1000000000
        if num / 1000000 != 0:
            ret += self.numberToWords(num / 1000000) + " Million "
            num %= 1000000
        if num / 1000 != 0:
            ret += self.numberToWords(num / 1000) + " Thousand "
            num %= 1000
        if num / 100 != 0:
            ret += self.numberToWords(num / 100) + " Hundred "
            num %= 100
        if num >= 20 and num / 10 != 0:
            ret += tens[num / 10 - 2] + " "
            num %= 10
            #print "...",ret, num
        if num != 0:
            ret += ones[num - 1]
            #print ret
        return ret.strip()

if __name__ == '__main__':
    nums = 1234567
    s = Solution()
    print "\nInteger %d to word is: %s " %(nums,s.numberToWords(nums))

