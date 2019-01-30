
# LC-056 is on same lines
# Given an array of meeting time intervals consisting of start and end times
#  [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#############################################################################

# https://nb4799.neu.edu/wordpress/?p=2205

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import *

class Solution(object):
    def minMeetingRooms(self, intervals):

        Sortedintervals = sorted(intervals, key=lambda x: x[0]) # Sort based on Start time - x[0]
        print Sortedintervals
        heap = []

        for i in Sortedintervals:

            if heap and i[0] >= heap[0]:
                heappop(heap)  # So if start time > MinHeap, then you can merge those two meeting. In other words pop that because in end we are giving len(heap) for MIN number of Rooms required.

            heappush(heap, i[1]) # MinHeap is created based on End time. We push endtime to heap and minHeapify anyways .. and make sure min stays on root
        return len(heap)

if __name__ == '__main__':

    s = Solution()
    intervals = [[0, 30], [15, 20], [5, 10]]
    print "\nMinimum rooms required: ",s.minMeetingRooms(intervals)

# Question: Why do we need to use Heap here? Why not just do like LC-056
