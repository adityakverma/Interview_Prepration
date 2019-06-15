
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#
#
#
# Note: Do not use the eval built-in library function.
####################################################################################################3

# Python O(n) Solution using recursion
# Similar to Basic Calculator II and I use recursion to handle bracket.

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c
            return sum(stack)
        return helper([], 0)

##############################################################3

class Solution_:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, stack, sign = 0, [], "+"
        s += ' '
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num, skip = self.calculate(s[i+1:])
                i += skip
            elif s[i] in '+-*/)' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                if s[i] == ')':
                    return sum(stack), i + 1
                num = 0
                sign = s[i]
            i += 1
        return sum(stack)

