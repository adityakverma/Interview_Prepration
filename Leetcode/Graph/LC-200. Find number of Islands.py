
#Iterate through each of the cell and if it is an island,
# do dfs to mark all adjacent islands, then increase the counter by 1.

class Solution():

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i< 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

#######################################################################



'''
# https://www.geeksforgeeks.org/find-number-of-islands/

# Program to count islands in boolean 2D matrix
class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell

        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)


    # The main function that returns count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island and increment island count
                    self.DFS(i, j, visited)
                    count += 1
        return count

if __name__ == '__main__':

    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print "\nNumber of islands is :",
    print g.countIslands()

#-------------------------------------------------

# What is the significance of using
# static int rowNbr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
# static int colNbr[] = {-1, 0, 1, -1, 1, -1, 0, 1};
#
# Answer:
# All possible combinations of -1, 0 and 1 for row and column, excluding (0,0)
# which is the current location.
# It is part of a for loop where k goes from 0 to 7, so the combinations
# will be (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1).

'''

########################################################################################################

# [Aditya]: I will say this is similar to connected component problem -  but here we just checking neighbours
# of specific cordinate (x,y) and not checking each cordinate of graph. Secondly its more like DFS problem THAN
# kind is graph problem ( Connected component style)

'''

    In MS-Paint, when we take the brush to a pixel and click, the color of the region of that pixel is replaced with a new selected color. 

Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all adjacent (top, bottom, left, and right) same colored pixels with the given color. If the adjacent pixels of the adjacent pixels also have the same color, their orig

inal color gets updated also and the chain goes on. Implement fillPaint function.

Example:

let screen = [

  [0,0,1,1,1,1],

  [0,0,2,2,2,2],

  [1,1,1,1,1,1],

  [3,3,1,1,3,3],

  [0,0,0,3,3,0],

];

let x = 3;

let y = 4;

let newColor = 4;

fillPaint(screen, x, y, newColor);

// output

[

  [0,0,1,1,1,1],

  [0,0,2,2,2,2],

  [1,1,1,1,1,1],

  [3,3,1,1,4,4],

  [0,0,0,4,4,0],

]


# ----------------------------------------------------------

function fillPaint(matrix, x, y, newColor) {

  let origColor = matrix[x][y];

  let fillPaintUtil = function(matrix, x, y, newColor, origColor) {

    if (x < 0 || y < 0 || x >= matrix[0].length || y >= matrix.length || matrix[x][y] !== origColor) {

      return;

    } else {

      matrix[x][y] = newColor;

    }

    fillPaintUtil(matrix, x - 1, y, newColor, origColor);

    fillPaintUtil(matrix, x + 1, y, newColor, origColor);

    fillPaintUtil(matrix, x, y - 1, newColor, origColor);

    fillPaintUtil(matrix, x, y + 1, newColor, origColor);

  }

  fillPaintUtil(matrix, x, y, newColor, origColor);

  return matrix;

}

let matrix = [

  [1,2,1,1,1,1,1,1],

  [1,2,1,1,1,1,1,1],

  [1,2,1,1,1,1,1,2],

  [1,2,1,2,2,1,1,1],

  [1,2,1,1,2,1,1,1],

  [1,2,1,1,2,1,1,1],

  [1,2,1,1,2,1,2,1],

  [1,2,1,1,2,2,2,2]

]

console.log(fillPaint(matrix,3,4,3));


'''