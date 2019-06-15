
# Tags: Array, Sort, Google, FB, MS

# lc-253 IS SAME CONCEPT - BUT WE USED HEAP THERE ....

# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        ret = []

        for itv in intervals:
            start, end = itv.start, itv.end

            if not ret or ret[-1].end < start:
                ret.append(Interval(start, end))  # Append it to result now. Later it will be adjusted for end if required.
            else:
                ret[-1].end = max(ret[-1].end, end)
        return ret


        # Algorithm: 4/10/19
        # ==========
        # Step-1: Sort the intervals with respect to start time - intervals.sort(key=lamda x:x.start)
        # Step-2: Iterate over intervals and
        #   if either result is empty OR last element of result.end is < current_interval.start then just "APPEND THAT INTERVAL" to result
        #   else "COMBINE" - adjust result[-1].end as max(result[-1].end or current_interval.end) - meaning combining or merging two intervals.

        # Time Complexity:
        # ================
        # Sorting takes O(n log(n)) and merging the intervals takes O(n). So, the resulting algorithm takes O(n log(n)).
        # Other Similar Problems: 252 Meeting Rooms, 253 Meeting Rooms II, 435 Non-overlapping Intervals,

        # Concept:
        # ========
        # Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.


# ===================================================================
class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                 merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1]) # chooses 6, 13
        return merged

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 13], [9, 12], [2, 5], [15, 18]]

    print "TEST", intervals[-1], intervals[-1][1]
    s = Solution1()
    print s.merge(intervals)


# Complexity Analysis
#
#     Time complexity : O(nlgn)
#     Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by
#     the O(nlgn) complexity of sorting.
#
#     Space complexity : O(1) (or O(n))
#     If we can sort intervals in place, we do not need more than constant additional space.
#     Otherwise, we must allocate linear space to store a copy of intervals and sort that.
