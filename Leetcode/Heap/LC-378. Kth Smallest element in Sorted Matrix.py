
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.

from heapq import *

# I believe the complexity should be O(nlogk) for an nxn matrix.
# At most, n elements in the heap.

class Solution():

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        min_heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(min_heap, matrix[i][j])

        while k > 1:
            heappop(min_heap)
            k -= 1

        return min_heap[0]  #OR return heappop(min_heap)

    # O(n+k)(log n)

if __name__ == '__main__':

    s = Solution()

    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 8

    print "\nKth smallest is",s.kthSmallest(matrix, k)


'''

# Future Studies / research 

# Balaji's

from Queue import PriorityQueue
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        tmatrix = [[True] * n for i in range(m)]
        q = PriorityQueue()
        q.put((matrix[0][0], [0,0]))
        count = 0
        kth = None
        while(count < k):
            val, mn = q.get()
            if mn[0] + 1 < m and tmatrix[mn[0]+1][mn[1]] :
                q.put((matrix[mn[0]+1][mn[1]], [mn[0]+1, mn[1]]))
                tmatrix[mn[0]+1][mn[1]] = False
                
            if mn[1] + 1 < n and tmatrix[mn[0]][mn[1]+1]:
                q.put((matrix[mn[0]][mn[1]+1], [mn[0], mn[1]+1]))
                tmatrix[mn[0]][mn[1]+1] = False
            count += 1
            kth = val
            #print val
       
        return kth

# ---------------------------------------------------------------------        
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85219/Python-solution-O(klogk)-similar-to-problem-373
# Python solution O(klogk) similar to problem 373

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1
        return result
    
# Since the matrix is sorted, we do not need to put all the elements in heap at one time. We can simply pop and put for k times. By observation, if we look at the matrix diagonally, we can tell that if we do not pop matrix[i][j], we do not need to put on matrix[i][j + 1] and matrix[i + 1][j] since they are bigger.
# 
# e.g., given the matrix below:
# 1 2 4
# 3 5 7
# 6 8 9
# We put 1 first, then pop 1 and put 2 and 3, then pop 2 and put 4 and 5, then pop 3 and put 6...
                    
'''