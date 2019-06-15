
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# [Aditya]: Note we used rows and column instead of x and y. See the tips from gayle to avoid confusion.

# https://leetcode.com/problems/spiral-matrix/discuss/137031/Easy-to-Understand-Python-Solution
class Solution():
    # My solution  involves looping in the spiral manner, and appending the value to result.
    def spiralOrder(self, matrix):

        res = []
        expectedlength = len(matrix[0]) * len(matrix)

        startCol = 0
        endCol = len(matrix[0]) - 1

        startRow = 0
        endRow = len(matrix) - 1

        if len(matrix) == 0:
            return res

        while (startCol <= endCol and startRow <= endRow):

            # Traverse Right
            for i in range(startCol, endCol + 1):
                res.append(matrix[startRow][i])

            startRow += 1

            if len(res) == expectedlength: break

            # Traverse Down
            for i in range(startRow, endRow + 1):
                res.append(matrix[i][endCol])

            endCol -= 1

            if len(res) == expectedlength: break

            # Traverse Left
            for i in range(endCol, startCol - 1, -1):
                res.append(matrix[endRow][i])

            endRow -= 1

            if len(res) == expectedlength: break

            # Traverse Up
            for i in range(endRow, startRow - 1, -1):
                res.append(matrix[i][startCol])

            startCol += 1
        return res

if __name__ == '__main__':

    matrix = [
              [ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]
            ]
    s = Solution()
    print "\nSpiral Matrix:",s.spiralOrder(matrix)



# https://leetcode.com/problems/spiral-matrix/discuss/20793/7-lines-recursive-python-solution-(+-5-lines-solution-wo-recursion)
# https://leetcode.com/problems/spiral-matrix/discuss/20821/An-iterative-Python-solution
# https://leetcode.com/problems/spiral-matrix/discuss/20783/Short-concise-python-solution-(14lines)

# https://leetcode.com/problems/spiral-matrix/discuss/20862/Simple-Python-solution-using-one-for-loop
