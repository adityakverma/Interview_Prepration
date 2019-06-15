

# Python simple dfs solution
# https://leetcode.com/problems/word-search/discuss/27665/Python-simple-dfs-solution

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


    def searchWord_helper(self, board, word, i, j):

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

            board[i][j] = word[0]  # update the cell to its original value
            return False
        else:
            return False

###########################################################################
#https://leetcode.com/problems/word-search/discuss/27820/Python-DFS-solution

class Solution2():

    def exist(self, board, word):
        if not board:
            return False
        r, c = len(board), len(board[0])
        visited = [[False for i in xrange(c)] for j in xrange(r)]
        for i in xrange(r):
            for j in xrange(c):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, i, j):
        if not word:
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
                or visited[i][j] or word[0] != board[i][j]:
            return False
        visited[i][j] = True
        res = self.dfs(board, word[1:], visited, i + 1, j) or \
              self.dfs(board, word[1:], visited, i - 1, j) or \
              self.dfs(board, word[1:], visited, i, j - 1) or \
              self.dfs(board, word[1:], visited, i, j + 1)
        visited[i][j] = False
        return res

##########################################################################



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