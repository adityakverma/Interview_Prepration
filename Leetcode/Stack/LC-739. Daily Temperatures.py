
# Given a list of daily temperatures T, return a list such that, for each day
#  in the input, tells you how many days you would have to wait until a warmer
# temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# =================================================================================

class Solution(object):

    def dailyTemperatures(self, temps):

        if not temps:
            return []

        result = [0] * len(temps)
        stack = []

        for curr_idx, curr_temp in enumerate(temps):

            while stack and curr_temp > stack[-1][1]:
                last_idx, last_temp = stack.pop()
                result[last_idx] = curr_idx - last_idx

            stack.append((curr_idx, curr_temp))

        return result

# ====================================================================================

# https://leetcode.com/problems/daily-temperatures/discuss/165974/Python-stack-solution-similar-to-%22Largest-Rectangle-in-Histogram%22-problem
#This is similar to the answer on the solution page but I think this one is easier to read.
# Here is the discussion from problem 84 "Largest Rectangle in Histogram" that helped me
# learn how to approach this type of problem: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/153055/Really-short-python-solution-using-stack

