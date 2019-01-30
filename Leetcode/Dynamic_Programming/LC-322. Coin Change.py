
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# -----------------------------------------------------------

# This can be understood with Greedy, but its not good idea to implement using GREEDY, so we use DP

class Solution(object):
    def coinChange(self, coins, totalamount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or totalamount == 0:
            return 0

        dp = [totalamount + 1 for _ in range(totalamount + 1)]
        dp[0] = 0

        for amount in range(1, totalamount + 1):
            for coin in coins:
                # print "coin", amount, coin
                if amount >= coin:
                    # print dp[amount], dp[amount-coin], amount, coin
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
            # print('dp:', dp)

        if dp[totalamount] > totalamount:
            return -1
        else:
            return dp[totalamount]


''' 
Suppose you're given coins [1, 2, 5], and you want to make 11. What's the smallest 
amount of coins you need to do this?
Well, lets suppose I take 1. Then, what's the smallest amount of coins I need to make 
11 - 1 = 10? Certainly, if I take 1, then the solution will be 1 + smallest amount of 
coins I need to make 10.

Similarly, if I take 2, the solution will be 1 + smallest amount of coins I need to make 9.
And finally, if I take 5, the solution will be 1 + smallest amount of coins I need to make 6.

So, the best solution will be the minimum of the smallest amount of coins I need to make 
6, 9 or 10. You can repeat this idea recursively until you reach the base case of "how 
many coins do I need to make 0", in which case 0, or "how many coins do I need to make -1",
 in which case no amount of coins will ever make -1, so an arbitrarily large number is a 
 suitable choice. '''

