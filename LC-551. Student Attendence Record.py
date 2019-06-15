
# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
#
#     'A' : Absent.
#     'L' : Late.
#     'P' : Present.

# A student could be rewarded if his attendance record doesn't contain more than one 'A'
# (absent) or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance
# record.
#
# Example 1: Input: "PPALLP"
# Output: True
#
# Example 2: Input: "PPALLL"
# Output: False
# ----------------------------------------------------------------------------------


class Solution(object):

    def checkRecord(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
                if count > 1:
                    return False
            else:
                if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                    return False
        return True

    def checkRecord1(self, s):
        if s.count('A') > 1 or "LLL" in s :
            return False
        else :
            return True

    def checkRecord2(self, s):
        absent, late = 0, 0
        for c in s:
            if c == 'A':
                absent += 1

            if c == 'L':
                late += 1
            else:
                late = 0

            if absent > 1 or late > 2:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    input = "PPALLP"
    print "\nCan be rewarded:",s.checkRecord(input)


