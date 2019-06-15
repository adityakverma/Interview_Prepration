
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


class Solution():

    # https://leetcode.com/problems/multiply-strings/discuss/17675/14-line-Python-solution-handwritten-approach-simulation

    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        data = [0] * (len(num1) + len(num2) + 1)
        #print "Data", data, len(data)

        ans = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                data[i + j] += int(num1[i]) * int(num2[j])
                #print i+j, data[i+j]

        carry = 0
        #print "Data... ", data, len(data)

        for k in range(len(data)):
            mod = (carry + data[k]) % 10
            carry = (carry + data[k]) / 10
            #print "mod, carry",mod, carry
            ans.append(str(mod))
            #print "append mod",ans
        if carry:
            ans.append(str(carry))
            #print "carry", ans

        ans = ans[::-1]
        #print "rev...", ans
        while (ans[0] == '0' and len(ans) > 1):
            ans.pop(0)

        return "".join(ans)

    # Don't know if this satisfies the description... accepted though.
    def multiply1(self, num1, num2):
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9} # Note this map char to int, instead of typecastinf using int. smart way
        n1 = num1[::-1]
        n2 = num2[::-1]
        sum1 = 0
        sum2 = 0
        for i in range(len(n1)):
            sum1 += d[n1[i]] * (10 ** i) # Note: 10*2 = 20, but 10**2 = 100
        for i in range(len(n2)):
            sum2 += d[n2[i]] * (10 ** i)
        #print sum1, sum2
        return str(sum1 * sum2)

    def multiply_stupidway(self, num1, num2):
        return str(long(num1) * long(num2))

if __name__ == '__main__':
    s = Solution()
    num1 = "12"
    num2 = "11"
    print "\nProduct is\n",s.multiply(num1,num2)
    print "\nProduct is\n",s.multiply_stupidway(num1,num2)
