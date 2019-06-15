
# Given a 2D integer matrix M representing the gray scale of an image, you need to design
# a smoother to make the gray scale of each cell becomes the average gray scale (rounding down)
# of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells,
# then use as many as you can.

# Example 1:
#
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

######################################################################################

# Intuition and Algorithm :

# For each cell in the grid, look at the immediate neighbors - up to 9 of them, including the original cell.
# Then, we will add the sum of the neighbors into ans[r][c] while recording count, the number of such neighbors.
# The final answer is the sum divided by the count.


class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]
        #print ans

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        #print "Here", nr,nc
                        if 0 <= nr < R and 0 <= nc < C:
                            #print "......Within......", nr,nc,  r,c
                            ans[r][c] += M[nr][nc]
                            #print "ans is ...",ans
                            count += 1
                            #print "Count", count
                #print "PRE ans", ans
                ans[r][c] /= count
                #print "POST and", ans

        return ans



if __name__ == '__main__':

    matrix = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    s = Solution()
    print "\nImage Smoother: \n",s.imageSmoother(matrix)