
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
# ------------------------------------------------------------------------

# Iterate through each of the cell and if it is an island, do dfs to mark all
# adjacent islands, then increase the counter by 1.

class Solution():

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Only once this will happen on first 1, remaining neighbours will be tagged with '#' so they dont contribute to count++
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i< 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#' # Tagging visited coordinate, so we don't revisit. and do false count++ in above code.
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

############################################################################




