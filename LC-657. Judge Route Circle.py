
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if
# this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true
#
# Example 2:
# Input: "LL"
# Output: false

import collections

class Solution():
    def JudgeCircle_Aditya(self,str): # Yey ! Accepted in first attempt : But issue I think not proper testcase # UL also gives 0. lol
        sum = 0
        dic = {"U":1,"D":-1,"L":-1,"R":1}
        for i in str:
            sum += dic[i]
        if sum != 0:
            return False
        return True


    def judgeCircle(self, moves):  # BETTER Solution ....
        direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
        return 0 == sum(direct[m] for m in moves)

    def judgeCircle1(self, moves):  # Cannot use counter in interviews
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']



if __name__ == '__main__':
    str = "UDLR"
    s = Solution()
    print "\nDid we make circle:",s.judgeCircle(str)
