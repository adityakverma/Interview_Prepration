
# Tags: String, Facebook
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
# Given an integer n, generate the nth term of the count-and-say sequence.
# Note: Each term of the sequence of integers will be represented as a string.

# https://leetcode.com/problems/count-and-say/discuss/16382/Python-accepted-solution.
# https://leetcode.com/problems/count-and-say/discuss/16435/Python-Solution

class Solution():
    def countAndSay(self, n):
        res = "1"
        for _ in range(n -1):  # [Aditya]: Basically it means  we arnt using the value, we want to do something unrelated - for range(n-1) times.
            res = self.helper(res)
        return res

    def helper(self, n):
        count, i, res = 1, 0, ""
        #print "n", n
        while i < len(n) - 1:
            if n[i] == n[i + 1]:
                count += 1
                #print "if count", count
            else:
                res += str(count) + n[i]
                count = 1
                #print "else count",count
            i += 1
        #print "Before", res
        res += str(count) + n[i] # Concatnating the last ones.
        #print "After", res
        return res

if __name__ == '__main__':
    s = Solution()
    n = 4
    print "\n%dth term is: %s" %(n,s.countAndSay(n))

# At the beginning, I got confusions about what is the nth sequence. Well, my solution is accepted now, so I'm going to give some examples of nth sequence here. The following are sequence from n=1 to n=10:
#
#  1.     1
#  2.     11
#  3.     21
#  4.     1211
#  5.     111221
#  6.     312211
#  7.     13112221
#  8.     1113213211
#  9.     31131211131221
#  10.   13211311123113112211
#
# From the examples you can see, the (i+1)th sequence is the "count and say" of the ith sequence!

# NOTE:
# https://www.quora.com/What-does-_-in-Python-mean-in-a-for-loop
# "_" is just a convention which indicates that you wont be needing the iterator variable inside the loop for any operations.
# Iterator variable needed: Sum up first 5 whole numbers
#
#     total = 0
#     for i in range(5):
#         total += i
# -----------------------
# Iterator variable not needed: Sum up 1 five times
#
#     total = 0
#     for _ in range(5):
#         total += 1

# Underscore: https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc