
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
# be validated according to the following rules:
#
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
#     without repetition.
# =======================================================================

# MOST  INTERESTING - BIG O:
# TIME COMPLEXITY : O(1)
# SPACE COMPLEXITY : O(1)
# -------------------------


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

    # TO understand this code, just see the illustration under Solution Section.

# ------------------------------------------------------------------------------------------

class Solution_(object):
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            visited = set()
            for val in row:
                if val != '.':
                    if val in visited: return False
                    visited.add(val)

        # Check cols
        for j in xrange(9):
            visited = set()
            for i in xrange(9):
                val = board[i][j]
                if val != '.':
                    if val in visited: return False
                    visited.add(val)

        # Check grids
        for rowStart in xrange(0, 7, 3):
            for colStart in xrange(0, 7, 3):
                visited = set()

                for i in xrange(rowStart, rowStart + 3):
                    for j in xrange(colStart, colStart + 3):
                        val = board[i][j]
                        if val != '.':
                            if val in visited: return False
                            visited.add(val)

        return True


