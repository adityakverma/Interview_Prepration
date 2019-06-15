
# Tags: Array, Dymanic Programming, Amazon

# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost
# to reach the top of the floor, and you can either start from the step with index 0, or the
# step with index 1.
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
#
# Note:
#
#     cost will have a length in the range [2, 1000].
#     Every cost[i] will be an integer in the range [0, 999].

#####################################################################################################

# There is a clear recursion available: the final cost f[i] to climb the staircase from some step i is
# f[i] = cost[i] + min(f[i+1], f[i+2]). This motivates dynamic programming.

# Algorithm. FYI - This is editorial Solution
# Let's evaluate f backwards in order. That way, when we are deciding what f[i] will be, we've already figured out f[i+1] and f[i+2].
# We keep these updated as we iterate through i

class Solution(object):

    def minCostClimbingStairs1(self, cost_list):

        n = len(cost_list)   # Base case
        if n == 0 or n == 1:
            return 0

        f1 = f2 = 0
        for cost in cost_list:
            f0 = cost + min(f1, f2)
            f2 = f1
            f1 = f0
        return min(f1, f2)

    def minCostClimbingStairs2(self, cost):
        n = len(cost)   # Base case
        if n == 0 or n == 1:
            return 0

        min_cost0, min_cost1 = cost[0], cost[1]
        for c in cost[2:]:
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + c
        return min(min_cost0, min_cost1)


if __name__ == '__main__':
    cost =  [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    print "\nMinimum cost is ", s.minCostClimbingStairs1(cost)
    print "\nMinimum cost is ", s.minCostClimbingStairs2(cost)


# Complexity Analysis
    # Time Complexity: O(N) where NNN is the length of cost.
    # Space Complexity: O(1), the space used by f1, f2.
