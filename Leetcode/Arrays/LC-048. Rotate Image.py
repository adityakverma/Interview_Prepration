
# https://leetcode.com/problems/rotate-image/discuss/130144/Simple-Python-Solution-with-comments

class Solution(object):

    # ----------------------------------------------------------------------------

    def rotate_90Right(self, matrix):

        # Step-1: First transpose the matrix ( using diagonal from top left to right bottom)
        # Step-2: Flip it horizontally (across the mid column)
        # This gives RIGHT rotated matrix.

        n = len(matrix)
        for i in range(0,n):
            for j in range(0,i):  # from i to n coz we are flipping across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print "\nTranspose Matrix (Right)", matrix

        # Flip it horizontally (across the mid column)
        for i in range(0,n):
            for j in range(0, n/2 ):  # from i to n/2 coz we are flipping across the mid column
                matrix[i][j],matrix[i][ n - 1 -j] = matrix[i][ n - 1 -j], matrix[i][j]

        print "\nRotate 90 Right", matrix

    # ----------------------------------------------------------------------------
    def rotate_90Left(self, matrix):

        # Step-1: First transpose the matrix ( using diagonal from top right to left bottom) and
        # Step-2: Flip it horizontally (across the mid column)
        # This gives LEFT rotated matrix.

        n = len(matrix)
        for i in range(0,n):
            for j in range(i ,n):  # from i to n coz we are flipping across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print "\nTranspose Matrix (Left)", matrix

        # Flip it horizontally (across the mid column)
        for i in range(0,n/2):
            for j in range(0, n ):  # from i to n/2 coz we are flipping across the mid column
                matrix[i][j],matrix[n - 1 -i][ j] = matrix[n - 1 -i][ j], matrix[i][j]

        print "\nRotate 90 Left", matrix

    # ----------------------------------------------------------------------------

    def rotateMatrix180(self, matrix):
        length = len(matrix)

        for i in range(length):
            for j in range(i +1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
            print "HEre", matrix[i]
        print "\nRotate 180", matrix

if __name__ == '__main__':

    matrix1 =  [[1,2,3],
               [4,5,6],
               [7,8,9]]

    matrix2 =  [[1,2,3],
               [4,5,6],
               [7,8,9]]
    s = Solution()
    s.rotate_90Right(matrix1)
    print "-----------------------------------------------"
    s.rotate_90Left(matrix2)

    #s.rotateMatrix180(matrix)

