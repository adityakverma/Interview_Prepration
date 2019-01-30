
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# ----------------------------------------------------------------------------
from heapq import *

# Interesting facts - Aditya:
# 1. Here, we are adding extra information to minHeap apart from value,
# which is pair used to get that value.
# 2. Somehow making minHeap for positive numbers does'nt work. It's not adding min
# value 2 again to minHEap. So we make minHeap by -ve values

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        result = []

        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k: # Keep pushing first kth pairs for sure - because we need to get atleast k pairs.
                    heappush(heap, (-n1-n2, [n1, n2]))
                    #print heap, heap[0][0]
                else:
                    if heap and -heap[0][0] > n1 + n2: # Now if we find any lower value than current heap root, then pop root and push that value. Important - Note we are only maintaining heap of size k.
                        heappop(heap)
                        heappush(heap, (-n1-n2, [n1, n2]))
                    else:
                        break

        for _ in range(k): # since we had kept our heap of only size k.
            if heap:
                result.append(heappop(heap)[1]) # Note heap[0] is value and heap[1] is pair of value which were added to get heap[0]
        return result

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2

    print "\nPairs with smallest sums are: ",s.kSmallestPairs(nums1, nums2, k)






















###############################################################
# Original code:
'''
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k, heap=[]):
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k: heapq.heappush(heap, (-n1-n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1-n2, [n1, n2]))
                    else: break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]

'''