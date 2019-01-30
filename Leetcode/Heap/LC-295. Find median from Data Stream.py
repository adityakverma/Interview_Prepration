
# Median is the middle value in an ordered integer list. If the size of the list is even,
#  there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.

# Example:
# addNum(1),  addNum(2), findMedian() -> 1.5
# addNum(3),  findMedian() -> 2

##############################################################################################

# [Aditya] : If this was a fixed lenth array then we could simply sorted array and given middle
# element for median. But since this is data stream, we need to continously maintain the MinHeap
# and MaxHeap. so eventually we take top from both heaps and get average to get median.

# This will help to maintain direct access to median elements at all times, and finding the median
# would take a constant amount of time.

# It turns out there are two data structures for the job:

#    Heaps (or Priority Queues 1)
#    Self-balancing Binary Search Trees

# Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic
# order of time. They also give direct access to the maximal/minimal elements in a group.

# If we could maintain two heaps in the following way:
#
#     A max-heap to store the smaller half of the input numbers
#     A min-heap to store the larger half of the input numbers
#
# This gives access to median values in the input: they comprise the top of the heaps!
#
# Wait, what? How?
#
# If the following conditions are met:
#
#     Both the heaps are balanced (or nearly balanced)
#     The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers
#
# then we can say that:
#
#     All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it xxx)
#     All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it yyy)
#
# Then xxx and/or yyy are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.
#
# This leads us to a huge point of pain in this approach: balancing the two heaps!


from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        # keep smaller half (size >= 1)
        self.maxHeap = []
        self.minHeap = []

    # Adding a number num:

    # 1. Add num to max-heap lo. Since lo received a new element, we must do a balancing step
    # for hi. So remove the largest element from lo and offer it to hi.
    # 2. The min-heap hi might end holding more elements than the max-heap lo, after the previous
    # operation. We fix that by removing the smallest element from hi and offering it to lo.
    #
    # The above step ensures that we do not disturb the nice little size property we just mentioned.

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        #print "Debug-1 MaxHeap", self.maxHeap
        heappush(self.minHeap, -heappop(self.maxHeap))
        #print "Debug-2 MinHeap", self.minHeap

        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

        print "\nMin Heap is :",self.minHeap
        print "Max Heap is :",self.maxHeap

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])

        return ((-self.maxHeap[0] + self.minHeap[0] + 0.00) / 2)

if __name__ == '__main__':
    Input = [41, 35, 62, 5, 97, 108]

    s = MedianFinder()
    for i in Input:
        s.addNum(i)

    print "\nMedian of stream: ",s.findMedian()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# -------------------------------------------------------------------

# A little example will clear this up! Say we take input from the stream [41, 35, 62, 5, 97, 108]. The run-though of the algorithm looks like this:
#
# Adding number 41
# MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
# MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
# Median is 41
# =======================
# Adding number 35
# MaxHeap lo: [35]
# MinHeap hi: [41]
# Median is 38
# =======================
# Adding number 62
# MaxHeap lo: [41, 35]
# MinHeap hi: [62]
# Median is 41
# =======================
# Adding number 4
# MaxHeap lo: [35, 4]
# MinHeap hi: [41, 62]
# Median is 38
# =======================
# Adding number 97
# MaxHeap lo: [41, 35, 4]
# MinHeap hi: [62, 97]
# Median is 41
# =======================
# Adding number 108
# MaxHeap lo: [41, 35, 4]
# MinHeap hi: [62, 97, 108]
# Median is 51.5

