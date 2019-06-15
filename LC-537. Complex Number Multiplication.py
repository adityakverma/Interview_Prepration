
# Tags: Math, Strings, AWS
#  Given two strings representing two complex numbers.
#
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#
# Example 1:
#
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
#
# Example 2:
#
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

# Algorithm
#
# Multiplication of two complex numbers can be done as:
# https://leetcode.com/problems/complex-number-multiplication/solution/#
# We simply split up the real and the imaginary parts of the given complex strings based on the '+' and the 'i' symbols. We store the real parts of the two strings aaa and bbb as x[0]x[0]x[0] and y[0]y[0]y[0] respectively and the imaginary parts as x[1]x[1]x[1] and y[1]y[1]y[1] respectively. Then, we multiply the real and the imaginary parts as required after converting the extracted parts into integers. Then, we again form the return string in the required format and return the result

class Solution(object):
    def complexNumberMultiply(self, a, b): # Aditya

        A = [int(x) for x in a.replace('i','').split('+')]
        B = [int(x) for x in b.replace('i','').split('+')]
        return str(A[0]*B[0]-A[1]*B[1])+'+'+str(A[0]*B[1]+A[1]*B[0])+'i'

    # https://leetcode.com/problems/complex-number-multiplication/discuss/135191/Python-with-and-without-re-support-versions
    def complexNumberMultiply1(self, a, b):
        import re
        mo = re.match(r'(-?\d+)\+(-?\d+)i', a)
        if not mo: return ""
        ar, ai = mo.groups()
        mo = re.match(r'(-?\d+)\+(-?\d+)i', b)
        if not mo: return ""
        br, bi = mo.groups()
        nr = int(ar) * int(br) - int(ai) * int(bi)
        ni = int(ar) * int(bi) + int(ai) * int(br)
        return "{}+{}i".format(nr, ni)

    def complexNumberMultiply2(self, a, b):
        ar, ai = a[:-1].split('+')
        br, bi = b[:-1].split('+')
        nr = int(ar) * int(br) - int(ai) * int(bi)
        ni = int(ar) * int(bi) + int(ai) * int(br)
        return "{}+{}i".format(nr, ni)

    def complexNumberMultiply3(self, a, b):
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        #return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)
        return "{r}+{i}i".format(r=a1 * b1 - a2 * b2, i=a1 * b2 + a2 * b1)

if __name__ == '__main__':
    a = "1+1i"
    b = "1+1i"
    s = Solution()
    print "\nComplex number multiplication:",s.complexNumberMultiply(a,b)
    print "\nComplex number multiplication:",s.complexNumberMultiply1(a,b)
    print "\nComplex number multiplication:",s.complexNumberMultiply2(a,b)
    print "\nComplex number multiplication:",s.complexNumberMultiply3(a,b)

# Complexity Analysis:
#     Time complexity : O(1). Here splitting takes constant time as length of the string is very small (<20)(<20)(<20).
#     Space complexity : O(1). Constant extra space is used.
