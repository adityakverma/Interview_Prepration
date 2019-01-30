
#
# The n-queens puzzle is the problem of placing n queens on an n*n chessboard such
# that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,' \
# ' where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
# ----------------------------------------------------------------------------------------

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.board = [["." for x in range(n)] for x in range(n)]
        self.n = n
        self.solve(0)
        return self.result

    def solve(self, col):
        if col == self.n:   # Simply append current solution to result.
            solution = []

            for row in self.board:
                string = ""
                for char in row:
                    string += char
                solution.append(string)

            self.result.append(solution)
            return

        for row in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = "Q"  # Choose
                self.solve(col +1)
                self.board[row][col] = "."  # Un-choose

    def isSafe(self, row, col):
        for c in range (col):                # We just check vertical columns fo that row. No need to check rows, as we keep 1 Q in each row
            if self.board[row][c] == "Q":
                return False

        rup = row -1
        rdown = row +1
        c = col -1
        while c >= 0:

            if rup >= 0:
                if self.board[rup][c] == "Q":   # 1st Diagonal
                    return False

            if rdown < self.n:
                if self.board[rdown][c] == "Q": # 2nd Diagonal
                    return False

            rup -= 1
            rdown += 1
            c -= 1
        return True

