
# Given two strings A and B, find the minimum number of times A has to be repeated
# such that B is a substring of it. If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (abcdabcdabcd), B is a substring of it;
# and B is not a substring of A repeated two times ("abcdabcd").

class Solution(object):

    # https://leetcode.com/problems/repeated-string-match/discuss/108078/Python-solution.
    def repeatedStringMatch3(self, A, B):   # ACCEPTED
        C = ""
        for i in range(len(B)/len(A) + 3):
            if B in C:
                return i
            C += A
        return -1

    # https://leetcode.com/problems/repeated-string-match/discuss/108098/Understandable-Python-Solution
    def repeatedStringMatch2(self, A, B):  # ACCEPTED

        temp = ""
        count = 0
        while len(temp) < len(B):
            temp+=A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        return -1

    def repeatedStringMatch1(self, A, B): # Aditya's. Few TC failing. Not Submitted
        if B in A:
            print "Here"
            return 1

        if A[0] != B[0] or (len(B) % len(A) != 0):
            minRepeat = len(B) / len(A) + 1
        else:
            minRepeat = len(B) / len(A)

        newA = A * minRepeat
        for i in range(len(newA)):
            if newA[i] == B[0]:
                for j in range(len(B)):
                    if B[j] != newA[i + j]:
                        return -1
                return minRepeat
        return -1

if __name__ == '__main__':
    s = Solution()
    A = 'abcd'
    B = 'cdabcdab'
    print "\nMin Repeat:",s.repeatedStringMatch1(A,B)
    print "\nMin Repeat:",s.repeatedStringMatch2(A,B)
    print "\nMin Repeat:",s.repeatedStringMatch3(A,B)




    # "abcabcabcabc"
    # "abac"
    #
    # "aa"
    # "a"
    #
    # "a"
    # "aa"
    #
    # "bb"
    # "bbbbbbb"

# Submission Result: Accepted
# Next challenges: Repeated Substring Pattern - LC-459




