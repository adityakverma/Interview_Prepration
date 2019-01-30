
# https://leetcode.com/problems/generate-parentheses/description/
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

############################ ACCEPTED #################################

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n < 1:
            return 0
        self.backtrack_LC022(n,0,[], res)
        return res

    def backtrack_LC022(self,n,start,cur, res):
        options = ['(',')']
        if start == 2*n:
            if self.isvalidParenthesis(cur):
                res. append(''.join(cur))
            return

        for ch in options:
            cur.append(ch)
            self.backtrack_LC022(n,start+1,cur, res)
            cur.pop()

    def isvalidParenthesis(self, s): #LC-020
        stack = []         # Basically we are treating list as stack here and using list functions like append(), pop().
        match = {'(': ')'}

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack


# --------------------------------------------------------------
# Brute Force Method
# ---------------------------------------------------------------

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    print "A",A
                    ans.append("".join(A))
            else:
                A.append('(')
                print ".. append (", A
                generate(A)
                A.pop()
                print "pop", A

                A.append(')')
                print " -- APPEND(", A
                generate(A)
                A.pop()
                print " - POP", A

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

# Complexity Analysis
# https://leetcode.com/problems/generate-parentheses/solution/#

# --------------------------------------------------------------
# Backtracking Method
# ---------------------------------------------------------------

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

s = Solution()
print "\nBacktracking",s.generateParenthesis(3)

# DP
# https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
# https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation



