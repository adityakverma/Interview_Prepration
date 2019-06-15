#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
#     Rule 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#     Rule 2. Any live cell with two or three live neighbors lives on to the next generation.
#     Rule 3. Any live cell with more than three live neighbors dies, as if by over-population..
#     Rule 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# -----------------------------------------------------------------------------------------

# The idea is to use the second bit to store the updated state for each cell during the updating process.
# When the updating is finished, move 2nd bit to the first bit.

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        # calculate the number of live neighbors for cell (i,j)
        # the key point is to understand that the change to a cell is only decided by its nearby 8 cell in the original grid.
        # we should not use the updated cell to compute to change decision for other cell. So we do in-place with using intermediate grid

        def findLiveNeighbor(board, i, j):
            count = 0
            for a, b in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                         (i, j - 1), (i, j + 1)]:
                if a >= 0 and a < len(board) and b >= 0 and b < len(board[0]) and board[a][b] % 2 == 1: # board[p][q] % 2 remains the original 0/1 of each cell.

                    # Counting neighbors means extending existing conditions to account for that
                    count += 1
            return count

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                liveNeighbors = findLiveNeighbor(board, i, j)

                # Rule 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                # Rule 2. Any live cell with two or three live neighbors lives on to the next generation.

                if board[i][j] == 0 and liveNeighbors == 3 or board[i][j] == 1 and liveNeighbors in [2, 3]:
                    board[i][j] |= 2

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] >>= 1
        return

'''
In order implement the in-place algorithm, we need to memorize the variation of neigbors. Here is the strategy,
Given a cell board[i][j], we visit each of its 8 neighbors,
if board[i][j] changes from 0 -> 1, then all the neighbors +2.
if board[i][j] changes from 1->0, then all the neighbors -2.
We could find that the board[p][q] // 2 memorizes the variation of '1''s of (p,q)'s neighbors, while board[p][q] % 2 remains the original 0/1 of each cell.

'''
