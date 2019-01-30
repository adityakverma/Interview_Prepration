
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.
#
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1
# --------------------------------------------------------------------------------

class Solution(object):

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # use dp[i] to represent how many ways to fill a backpack with capacity i
        # dp[0] should be initialized to 1 - it means there is one way (choose nothing) to fill

        dp = [1] + [0] * amount

        for coin in coins:
            for i in range(coin,
                           amount + 1):  # no of coins for amount j= no of coins for amount j + (no of coins needed for amount j-coins[i])
                dp[i] += dp[i - coin]

        return dp[-1]


