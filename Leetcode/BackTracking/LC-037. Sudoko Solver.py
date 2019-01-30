
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
# Empty cells are indicated by the character '.'.
# ---------------------------------------------------------------------

class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()

        if row == -1 and col == -1: # no unassigned position is found, puzzle solved
            return True

        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isSafe(row, col, num):  # Validate if no. is safe to put in that position(row, col, sub-square), then use BT to place num

                # Backtracking
                self.board[row][col] = num  # choose num at that position. And keep solving further for other positions (row, col)
                if self.solve():            # Keep solving further
                    return True
                self.board[row][col] = "."  # unchoose num at that position

        return False



    def isSafe(self, row, col, ch):
        boxrow = row - row % 3 # Fact we are subtracting the modulo here is taken care later in checksquare() when we do row+3, col+3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True


