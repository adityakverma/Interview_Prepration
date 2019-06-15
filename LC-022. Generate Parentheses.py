
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses. For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    #print "A",A
                    ans.append("".join(A))
            else:
                A.append('(')
                #print ".. append (", A
                generate(A)
                A.pop()
                #print "pop", A

                A.append(')')
                #print " -- APPEND(", A
                generate(A)
                A.pop()
                #print " - POP", A

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

if __name__ == '__main__':
    s = Solution()
    print "\nBrute Force \n", s.generateParenthesis(3)
