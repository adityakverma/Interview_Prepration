
# Tags: Array, Binary Search Tree, Google

#  Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.
# Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
# A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
# For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true  <=== Double booked
# MyCalendar.book(5, 15); // returns false  <=== can't be booked, because it would result in a triple booking
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
# -----------------------------------------------------------------------------------------------------------

# Intuition
# Maintain a list of bookings and a list of double bookings. When booking a new event [start, end),
# if it conflicts with a double booking, it will have a triple booking and be invalid.
# Otherwise, parts that overlap the calendar will be a double booking.

# Algorithm
# Evidently, two events [s1, e1) and [s2, e2) do not conflict if and only if one of them starts after
#  the other one ends: either e1 <= s2 OR e2 <= s1. By De Morgan's laws, this means the events conflict when s1 < e2 AND s2 < e1.

# If our event conflicts with a double booking, it's invalid. Otherwise, we add conflicts with the calendar
# to our double bookings, and add the event to our calendar.

# Time Complexity: O(N^2). for each book operation, it is O(N) and and there are N of them so N^2

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []  # List for Original Booking
        self.overlaps = []  # List for Double Booking

    def book(self, start, end):

        for i, j in self.overlaps:
            if start < j and end > i:  # If end is greater that start of another booking in overlap list then its third booking, so return False
                return False

        for i, j in self.calendar:     # Simple: If end is greater that start of another booking in calender list then its second booking, so append it to overlap list
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))  # If none, then its first booking and append to calender. Return True
        return True


if __name__ == '__main__':
    m = MyCalendarTwo()
    print "\nBooking (10,20): ",m.book(10,20)
    print "Booking (50,60): ",m.book(50,60)
    print "Booking (10,40): ",m.book(10,40)  # <==== Double Booking
    print "Booking (5, 15): ",m.book(5,15)   # <==== Triple Booking so False
    print "Booking (5, 10): ",m.book(5,10)
    print "Booking (25,55): ",m.book(25,55)

# We store an array self.overlaps of intervals that are double booked, and self.calendar for
# intervals which have been single booked. We use the line start < j and end > i to check if
# the ranges [start, end) and [i, j) overlap.
#
# The clever idea is we do not need to "clean up" ranges in calendar: if we have [1, 3] and [2, 4],
# this will be calendar = [[1,3],[2,4]] and overlaps = [[2,3]]. We don't need to spend time
# transforming the calendar to calendar = [[1,4]]






