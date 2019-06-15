
# https://leetcode.com/problems/my-calendar-i/solution/#
# Actually My Calender II was asked in google ...

#  Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
#
# Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
#
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# -----------------------------------
# This is O(log N) Solution

class MyCalendar:
    def __init__(self):
        self.timeline = []

    def binary_search(self, start_point):
        # returned value may be greater than the len(start_point) - 1
        # if point not in timeline, the position to be inserted.

        s = 0
        e = len(self.timeline) - 1
        while s <= e:
            mid = (s + e) // 2
            if self.timeline[mid][0] < start_point:
                s = mid + 1
            elif self.timeline[mid][0] > start_point:
                e = mid - 1
            else:
                return mid
        return s

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        Idea:
        Return false if
        the ending of last s is greater than current s
        the starting of next s is less than current ending

        Corner case: when the ending is the same as
            starting of the current interval being inserted

        Data Structure:
        self.timeline[i] = (staring time, ending time)

        [2, 4) [5, 7)
        [3, 5)
        """
        i = self.binary_search(start)

        # self.timeline[i] (start time, end time)
        if i < len(self.timeline) and self.timeline[i][0] < end:
            return False
        if i - 1 >= 0 and self.timeline[i - 1][1] > start:
            return False

        if i - 1 >= 0 and self.timeline[i - 1][1] == start:
            self.timeline[i - 1][1] = end
        self.timeline.insert(i, [start, end])

        return True

# ------------------------------------------------------
# Time Complexity: O(N)

# Algorithm
# We will maintain a list of interval events (not necessarily sorted). Evidently, two events [s1, e1)
# and [s2, e2) do not conflict if and only if one of them starts after the other one ends: either
# e1 <= s2 OR e2 <= s1. By De Morgan's laws, this means the events conflict when s1 < e2 AND s2 < e1.

class MyCalendar_(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            #print s, e
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True

if __name__ == '__main__':
    cal = MyCalendar_()
    print cal.book(10,20)
    print cal.book(15,25)
    print cal.book(20,30)
    print cal.book(30,50)



    # Time Complexity: O(N2), where N is the number of events booked.
    # For each new event, we process every previous event to decide whether the new event can be booked.
    #  This leads to O(N2)complexity.
    #
    # Space Complexity: O(N)O(N)O(N), the size of the calendar.


######################################################
# https://leetcode.com/problems/my-calendar-i/solution/#
# https://leetcode.com/problems/my-calendar-i/discuss/109476/Binary-Search-Tree-python

# Binary Tree Approach

class Node(object):
    def __init__(self, start, end):  # Modified node of Binary Tree with two fields start and end.
        self.s = start      # Filed within node
        self.e = end        # Field within node
        self.left = None    # Left child empty
        self.right = None   # Right child empty

    def insert(self, start, end):
        if self.s >= end:
            if self.left is None:   # That means you were successfully able to insert booking. Return True
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:       # That means you were successfully able to insert booking. Return True
            if self.right is None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False  # If we cannot insert either left or right, return False.


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:      # If first node of tree ( i.e 'root'), so make first node/booking and return true.
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)

if __name__ == '__main__':
    m = MyCalendar()
    print "\nBooking: ",m.book(10,20)
    print "\nBooking: ",m.book(10,15)

# Time Complexity (Python): O(N2) worst case with O(NlogN) on random data.
# For each new event, we insert the event into our binary tree. As this tree may not be balanced,
# it may take a linear number of steps to add each event.
# Space Complexity: O(N)O(N)O(N), the size of the data structures used.


