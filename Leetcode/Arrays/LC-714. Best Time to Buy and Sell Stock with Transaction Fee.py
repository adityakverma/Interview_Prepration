
# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee. You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a
# time (ie. you must sell the stock share before you buy again.). Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# O(n) time, O(1) space
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/116117/Python-greedy-solution-with-a-little-trick-(beats-98)-O(n)-time-O(1)-space

class Solution(object):
    def maxProfit(self, prices, fee):
        buy = prices[0]
        res = 0

        if not prices or len(prices) < 2: return 0
        for p in prices:
            #print "Start:  p, buy", p, buy
            if p < buy: # current price p is less than last buy, so set to lower buy
                buy = p # buy at p
                #print " Setting buy to lower val ",buy
            else:
                profit = p - buy - fee
                if profit > 0: # have profit
                    res += profit
                    buy = p - fee # [Aditya]: Trick - We do this, so we can again sell at higher price in future by setting buy to new p up in if statement. In other words, it will set new value of buy to lesser p ( which is 4) up in 'if' statement.
                    #print " == Result, profit, buy", res, profit, buy
        return res


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    s = Solution()
    print "\nNet Profit: ", s.maxProfit(prices,fee)

# That is the trick I was talking about. By setting the buy value to p - fee, we can handle the case of selling at the current price and the case of selling at a higher price in the future.
# Take prices = [1, 4, 3, 8, 9], fee = 2 as an example.
# At prices[1], the res becomes 1 because we buy at 1 and sell at 4. At this point, we set the buy variable to 4-2=2 (the price - the fee), which means selling in the future without any fee (because we have already sold it with the fee).


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/118234/Python-DP-solution

