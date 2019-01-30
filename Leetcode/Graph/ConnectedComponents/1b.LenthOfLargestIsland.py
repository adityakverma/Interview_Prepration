
# https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/

# Consider a matrix with rows and columns, where each cell contains either a 0 or a 1
# and any cell containing a 1 is called a filled cell. Two cells are said to be connected
# if they are adjacent to each other horizontally, vertically, or diagonally .If one or more
# filled cells are also connected, they form a region. find the length of the largest region.

# Examples:
#
# Input : M[][5] = { 0 0 1 1 0
#                    1 0 1 1 0
#                    0 1 0 0 0
#                    0 0 0 0 1 }
# Output : 6
# Ex: in the following example, there are 2 regions one with length 1 and the other as 6.
#     so largest region : 6
#--------------------------------------

# Idea is based on the problem or finding number of islands in Boolean 2D-matrix
# A cell in 2D matrix can be connected to at most 8 neighbors. So in DFS, we make
# recursive calls for 8 neighbors. We keep track of the visited 1s in every DFS
# and update maximum length region.
#
# Below is C++ implementation of above idea.
# // Program to find the length of the largest
# // region in boolean 2D-matrix
# #include<bits/stdc++.h>
# using namespace std;
# #define ROW 4
# #define COL 5
#
# // A function to check if a given cell (row, col)
# // can be included in DFS
# int isSafe(int M[][COL], int row, int col,
#            bool visited[][COL])
# {
#     // row number is in range, column number is in
#     // range and value is 1 and not yet visited
#     return (row >= 0) && (row < ROW) &&
#            (col >= 0) && (col < COL) &&
#            (M[row][col] && !visited[row][col]);
# }
#
# // A utility function to do DFS for a 2D boolean
# // matrix. It only considers the 8 neighbours as
# // adjacent vertices
# void DFS(int M[][COL], int row, int col,
#          bool visited[][COL], int &count)
# {
#     // These arrays are used to get row and column
#     // numbers of 8 neighbours of a given cell
#     static int rowNbr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
#     static int colNbr[] = {-1, 0, 1, -1, 1, -1, 0, 1};
#
#     // Mark this cell as visited
#     visited[row][col] = true;
#
#     // Recur for all connected neighbours
#     for (int k = 0; k < 8; ++k)
#     {
#         if (isSafe(M, row + rowNbr[k], col + colNbr[k],
#                                               visited))
#         {
#             // increment region length by one
#             count++;
#             DFS(M, row + rowNbr[k], col + colNbr[k],
#                                     visited, count);
#         }
#     }
# }
#
# // The main function that returns largest  length region
# // of a given boolean 2D matrix
# int  largestRegion(int M[][COL])
# {
#     // Make a bool array to mark visited cells.
#     // Initially all cells are unvisited
#     bool visited[ROW][COL];
#     memset(visited, 0, sizeof(visited));
#
#     // Initialize result as 0 and travesle through the
#     // all cells of given matrix
#     int result  = INT_MIN;
#     for (int i = 0; i < ROW; ++i)
#     {
#         for (int j = 0; j < COL; ++j)
#         {
#             // If a cell with value 1 is not
#             if (M[i][j] && !visited[i][j])
#             {
#                 // visited yet, then new region found
#                 int count = 1 ;
#                 DFS(M, i, j, visited , count);
#
#                 // maximum region
#                 result = max(result , count);
#             }
#          }
#     }
#     return result ;
# }
#
# // Driver program to test above function
# int main()
# {
#     int M[][COL] = { {0, 0, 1, 1, 0},
#                      {1, 0, 1, 1, 0},
#                      {0, 1, 0, 0, 0},
#                      {0, 0, 0, 0, 1}};
#
#     cout << largestRegion(M);
#
#     return 0;
# }

#########################################################################


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
    def DFS(self, i, j, visited, island_count):

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
                island_count += 1
                self.DFS(i + rowNbr[k], j + colNbr[k], visited, island_count)
        return island_count

    # The main function that returns count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        result = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island and increment island count
                    island = 1
                    island = self.DFS(i, j, visited, island)
                    count += 1
                    print island
                    result = max(result, island)
        return count, result

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

