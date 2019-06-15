
# Given a time represented in the format "HH:MM", form the next closest time by 
# reusing the current digits. There is no limit on how many times a digit can be reused.
# 
# You may assume the given input string is always valid. For example, "01:34", "12:09" 
# are all valid. "1:34", "12:9" are all invalid.
# 
# Example 1:
# 
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which 
# occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# 
# Example 2:
# 
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed 
# that the returned time is next day's time since it is smaller than the input time numerically.
# 
#########################################################################

class Solution(object):

    # Just turn the clock forwards one minute at a time until you reach a time with the original digits. OR
    # Simulate the clock going forward by 1 minute. Each time it moves forward, if all the digits are allowed, then return the current time.

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set(digit for digit in time.replace(":", ""))
        hour, minute = time.split(":")

        print digits
        print hour, minute

        while True:
            # Increment by one minute + handle minute 59 overflow
            if minute == '59':
                hour = str(int(hour) + 1)
                minute = '00'
            else:
                minute = str(int(minute) + 1)

            # Fix hour overflow 23 -> 00 if needed
            if int(hour) > 23:
                hour = '00'

            # Fill digits with zero if needed
            if len(hour) == 1:
                hour = '0' + hour
            if len(minute) == 1:
                minute = '0' + minute

            # print "====", digits, hour+minute

            if all(x in digits for x in hour + minute):
                return hour + ':' + minute

# Complexity Analysis
#
#     Time Complexity: O(1). We try up to 24∗6024 * 6024∗60 possible times until we find the correct time.
#
#     Space Complexity: O(1)

##############################################################
# "19:34"
#
# Your stdout
#
# set([u'1', u'9', u'3', u'4'])
# 19 34
# ==== set([u'1', u'9', u'3', u'4']) 1935
# ==== set([u'1', u'9', u'3', u'4']) 1936
# ==== set([u'1', u'9', u'3', u'4']) 1937
# ==== set([u'1', u'9', u'3', u'4']) 1938
# ==== set([u'1', u'9', u'3', u'4']) 1939
#
# Your answer
#
# "19:39"
#
# Expected answer
#
# "19:39"
