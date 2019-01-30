

# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
#     Players take turns placing characters into empty squares (" ").
#     The first player always places "X" characters, while the second player always places "O" characters.
#     "X" and "O" characters are always placed into empty squares, never filled ones.
#     The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
#     The game also ends if all squares are non-empty.
#     No more moves can be played if the game is over.
#
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
#
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
#
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# Explanation: Once Game is over which is done by X here so O cannot move
#
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
#  --------------------------------------------------------------------


class Solution(object):

    def get_count(self, board, char):
        count = 0
        for s in board:
            count += s.count(char)
        return count


    def check_win(self, board, char):

        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] == char):  # All same in horizontally
                return True

        for i in range(3):
            if (board[0][i] == board[1][i] == board[2][i] == char):  # All same in vertically
                return True

        if (board[0][0] == board[1][1] == board[2][2] == char):  # All same in diagonal (left top to right bottom)
            return True
        if (board[0][2] == board[1][1] == board[2][0] == char):  # All same in diagonal (right top to left bottom)
            return True


    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        o_count = self.get_count(board, 'O')
        x_count = self.get_count(board, 'X')

        if x_count - o_count > 1:  # Players take turns placing characters and X is first, so max difference can only be 1 and not more.
            return False
        if x_count < o_count:  # This is not possible because X always starts first.
            return False

        is_o_win = self.check_win(board, 'O')
        is_x_win = self.check_win(board, 'X')

        if is_o_win and is_x_win:  # Both can't win, because if X won then game is already over, so O can't play to win.
            return False

        if is_o_win:
            if x_count > o_count:  # If O won, then count of X can't be more because O only makes move after X, so both will have same count
                return False

        if is_x_win:
            if o_count == x_count:  # This is bad case because once X wins then O can't get change since gave is over, so False
                return False

        return True


#-------------------------------------------------------------------------------------------------

# See another problem - Design the Tic-Tac-toe



