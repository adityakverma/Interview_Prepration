
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]

# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# Doing it in-place (modifying same matrix) and not generating new matrix
# https://leetcode.com/problems/set-matrix-zeroes/discuss/26040/Very-Short-Python-Solution-with-O(1)-Space-Complexity.-13-Lines-of-Code.

class Solution():
    def SetMatrixZero(self,matrix):
        rowSet = set()
        colSet = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)

        # Change all rows containing 0 to 0
        for r in rowSet:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        # Change all columns containing 0 to 0
        for c in colSet:
            for r in range(len(matrix)):
                matrix[r][c] = 0

        return matrix

    # Complexity Analysis
    #
    #     Time Complexity: O(M x N) where M and N are the number of rows and columns respectively.
    #     Space Complexity: O(M + N)

if __name__ == '__main__':
    matrix = [
                [0,1,2,0],
                [3,4,5,2],
                [1,3,1,5]
            ]

    s = Solution()
    print s.SetMatrixZero(matrix)



# We can achieve O(1) space by keeping track of rows and columns
# to be erased (set to zero) within our matrix itself.
#
# The first row corresponds to the columns which needs to be 0.
# Simlarly, the first column determines which rows should be erased.
#
# If matrix[0][2] = None and matrix[1][0] = None
# this means column 2 and row 1 should be 0.
#
# Note that matrix[0][0] can correspond to both row 0 and column 0.
