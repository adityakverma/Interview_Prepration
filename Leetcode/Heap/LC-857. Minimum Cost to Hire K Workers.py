
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
#
# Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:
#
#     Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
#     Every worker in the paid group must be paid at least their minimum wage expectation.
#
# Return the least amount of money needed to form a paid group satisfying the above conditions.
#
#
#
# Example 1:
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
#
# Example 2:
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately
#-----------------------------------------------------------------------------------

# As in Approach #1, at least one worker is paid their minimum wage expectation.
#
# Additionally, every worker has some minimum ratio of dollars to quality that they demand. For example, if wage[0] = 100 and quality[0] = 20, then the ratio for worker 0 is 5.0.
#
# The key insight is to iterate over the ratio. Let's say we hire workers with a ratio R or lower. Then, we would want to know the K workers with the lowest quality, and the sum of that quality. We can use a heap to maintain these variables.
#
# Algorithm
# Maintain a max heap of quality. (We're using a minheap, with negative values.) We'll also maintain sumq, the sum of this heap.
# For each worker in order of ratio, we know all currently considered workers have lower ratio. (This worker will be the 'captain', as described in Approach #1.) We calculate the candidate answer as this ratio times the sum of the smallest K workers in quality.

# ----------------------------------------------------------------------------------
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

from heapq import *

class Solution(object):

    def mincostToHireWorkers(self, quality, wage, K):

        # Sort based on Ratio and we create minHeap based on ratio itself
        # because we like to choose min ratio so that ratio gets applied
        # to all and check conditions like ratio*quality >= his wage. We are
        # choosing min ratio because our aim is find minimum cost to hire
        # K worker.
        # Note: Heap will always be maintained of size K only.
        # so we keep finding for result using min ratio ( provided  conditions are met)
        # then keep sliding window to next K

        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality)) # Sort with respect to ratio, so we start with applying min ratio.
        print workers

        res = float('inf')
        qsum = 0
        heap = []

        for r, q in workers:
            heappush(heap, -q)

            qsum += q

            if len(heap) > K:      # If size of heap > K workers, so pop minimum, so we maintain heap of size k. This is like sliding window
                qsum += heappop(heap) # Remove that from qsum since popped is a negative value.

            if len(heap) == K:     # If size of heap is K workers, so try finding the result
                res = min(res, qsum * r) # Here when k =2, then that means we will use that ratio which will make sure r*quatiy > wage of all

        return res


#############################################################################################
# Explanation:
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/142100/My-Greedy-Python-solution-using-Maximum-Heap
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141771/Python-with-heapq
