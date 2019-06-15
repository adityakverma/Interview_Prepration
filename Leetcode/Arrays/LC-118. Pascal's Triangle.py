

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# https://www.youtube.com/watch?v=WP6qUluheoc&t=608s

# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution():

    def PascalTriangle(self,num): # My Solution
        res = [[0]*num for i in range(num)]

        if num <= 0: return []

        for i in range(num):
            res[i][0] = 1
            res[i][i] = 1

        for i in range(1,num):
            for j in range(1,num):
                res[i][j] = res[i-1][j-1]+ res[i-1][j]
        return res

    # https://leetcode.com/problems/pascals-triangle/discuss/38277/Simple-Python-4-lines
    def generatePascal(self,numRows):  # Same as my Solution

        if numRows <= 0: return []
        pascal = [[1] * (i + 1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal

    # https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.?page=2
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res

    # explanation:
    # Any row can be constructed using the offset sum of the previous row. Example:
    #         1 3 3 1 0
    #      +  0 1 3 3 1
    #      =  1 4 6 4 1

if __name__ == '__main__':

    num = 5
    s = Solution()
    print "\nSolution-1:",s.PascalTriangle(num)
    print "\nSolution-2:",s.generate(num)
    print "\nSolution-3:", s.generatePascal(num)