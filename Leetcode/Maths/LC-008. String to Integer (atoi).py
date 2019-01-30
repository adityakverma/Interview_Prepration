

import re

class Solution():

    def myAtoi(self, str):

        str = str.strip()
        str = re.findall('^[+\-]?\d+', str)

        try:
            res = int(''.join(str)) # Joining and typecasting

            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN:
                return MIN

            return res
        except:
            return 0

    # ------------------------------------------
    def myAtoi_(self, s):
        s = s.strip()
        try:
            val = ''
            for i in range(len(s)):
                if (s[i] in '+-' and i == 0) or '0' <= s[i] <= '9':
                    val += s[i]
                else:
                    break
            val = int(val)
            if val < -2 ** 31: return -2 ** 31
            if val > 2 ** 31 - 1: return 2 ** 31 - 1
            return val
        except:
            return 0


# The whole expression is (^[\+\-0]*\d+)\D*, where ^ matches the beginning of the
# string, [] matches any single character inside the bracket, * means preceding
# character [\+\-0] can be matched zero or more times, \d means decimal digits,
# + means preceding character \d must appear at least once.

# --------------
# . 	 Matches with any single character except newline char
# ? 	 match 0 or 1 occurrence of the pattern to its left
# + 	 1 or more occurrences of the pattern to its left
# * 	 0 or more occurrences of the pattern to its left
# \w 	 Matches with a alphanumeric character whereas \W (upper case W) matches non alphanumeric character.
# \d 	  Matches with digits [0-9] and /D (upper case D) matches with non-digits.
# \s 	 Matches with a single white space character (space, newline, return, tab, form) and \S (upper case S) matches any non-white space character.
# \b 	 boundary between word and non-word and /B is opposite of /b
# [..] 	 Matches any single character in a square bracket and [^..] matches any single character not in square bracket
# \ 	 It is used for special meaning characters like \. to match a period or \+ for plus sign.
# ^ and $ 	 ^ and $ match the start or end of the string respectively
# {n,m} 	 Matches at least n and at most m occurrences of preceding expression if we write it as {,m} then it will return at least any minimum occurrence to max m preceding expression.
# a| b 	 Matches either a or b
# ( ) 	Groups regular expressions and returns matched text
# \t, \n, \r 	 Matches tab, newline, return





