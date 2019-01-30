

# The n queens puzzle is the problem of placing n queens on an n*n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# --------------------------------------------------------------------------------------

class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.board = [["." for x in range(n)] for x in range(n)]
        self.n = n
        self.count = 0

        self.solve(0)

        return self.count

    def solve(self, col):
        if col == self.n:
            self.count += 1  # Same as LC-051, just put count instead of actual result.
            return

        for row in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = "Q"
                self.solve(col + 1)
                self.board[row][col] = "."

    def isSafe(self, row, col):
        for c in range(
                col):  # We just check vertical columns fo that row. No need to check rows, as we keep 1 Q in each row
            if self.board[row][c] == "Q":
                return False

        rup = row - 1
        rdown = row + 1
        c = col - 1
        while c >= 0:

            if rup >= 0:
                if self.board[rup][c] == "Q":  # 1st Diagonal
                    return False

            if rdown < self.n:
                if self.board[rdown][c] == "Q":  # 2nd Diagonal
                    return False

            rup -= 1
            rdown += 1
            c -= 1
        return True


