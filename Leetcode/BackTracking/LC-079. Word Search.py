
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be
# used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# --------------------------------------------------------------------------------

# ACCEPTED

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word): # If helper function returned False, then keep checking for other values of i & j.
                    return True
        return False

    # check whether can find word, start at (i,j) position. Note there only two places where this function can return.
    # 1. It can return TRUE if whole word is matched successfully
    # 2. Or it returns FALSE if meets boundary cond or mismatch or already visisted - In this case keep checking for other i and j's
    def dfs(self, board, i, j, word):

        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        tmp = board[i][j]  # first character is found, check the remaining part

        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp

        return res

# ====================================================================================






























































# Python simple dfs solution
# https://leetcode.com/problems/word-search/discuss/27665/Python-simple-dfs-solution

###########################################################################
#https://leetcode.com/problems/word-search/discuss/27820/Python-DFS-solution

class Solution2():

    def exist(self, board, word):
        if not board:
            return False

        visited = [[False for i in xrange(len(board))] for j in xrange(len(board[0]))] # this can avoid double visiting

        for i in range(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, i, j):

        if not word:  # If done checking all letters of word, then return true.
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
                or visited[i][j] \
                or word[0] != board[i][j]: # This is main check. If word[i] != board[i][j] then it would simply return False and game over. If not, keep looking in board.
            return False

        # Backtracking algorithm
        visited[i][j] = True # mark current position as visited. CHOOSE
        res = self.dfs(board, word[1:], visited, i + 1, j) or \
              self.dfs(board, word[1:], visited, i - 1, j) or \
              self.dfs(board, word[1:], visited, i, j - 1) or \
              self.dfs(board, word[1:], visited, i, j + 1)      # This checks in all neighbouring cells of board, if next letter of word is present or not.
        visited[i][j] = False # backtrack. UNCHOOSE

        return res

        # Note: word[1:] creates a new string from the 1st character in word to
        #  its end. For example, if you begin with word="hello", then calling
        # word[1:] will create a new string, "ello". As this process repeats
        # itself, you get a smaller and smaller string.

##########################################################################
###########################################################################
class Solution1():

    def searchWord(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for rows in range(len(board)):
            for cols in range(len(board[0])):
                if self.searchWord_helper(board, word, rows, cols):
                    return True
        return False

    def searchWord_helper(self, board, word, i, j):  # BACKTRACK + DFS

        if board[i][j] == word[0]:
            if not word[1:]:
                return True

            board[i][j] = " "  # indicate used cell

            # check all adjacent cells
            if i > 0 and self.searchWord_helper(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and self.searchWord_helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.searchWord_helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and self.searchWord_helper(board, word[1:], i, j + 1):
                return True

            board[i][j] = word[0]  # update the cell to its original value aka backtrack
            return False
        else:
            return False

#################################################################################

if __name__ == '__main__':

    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    word = "ABCCEDA"
    s1 = Solution1()
    s2 = Solution2()
    #print len(word),len(board), len(board[0])
    print "\nSolution-2 : ", s2.exist(board,word)
    print "\nSolution-1 : ", s1.searchWord(board,word)

#https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

# def exist(self, board, word):
#     if not board:
#         return False
#     for i in xrange(len(board)):
#         for j in xrange(len(board[0])):
#             if self.dfs(board, i, j, word):
#                 return True
#     return False
#
# # check whether can find word, start at (i,j) position
# def dfs(self, board, i, j, word):
#     if len(word) == 0: # all the characters are checked
#         return True
#     if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
#         return False
#     tmp = board[i][j]  # first character is found, check the remaining part
#     board[i][j] = "#"  # avoid visit agian
#     # check whether can find "word" along one direction
#     res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
#     or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
#     board[i][j] = tmp
#     return res