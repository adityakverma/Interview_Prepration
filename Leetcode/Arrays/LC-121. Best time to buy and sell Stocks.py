
# Tags: Array, DP, Facebook, MS, AWS

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell
# one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/122458/simple-python

class Solution:

    # Time Complexity O(n)
    def maxProfit(self, prices):  # NOTE : USE KADANE's algo only if values are negative

        if not prices or len(prices) < 2:
            return 0

        import sys
        lowestprice = sys.maxint

        maxprofit = 0
        for i in range(len(prices)):

            if prices[i] < lowestprice:
                lowestprice = prices[i]

            if prices[i] - lowestprice > maxprofit:
                maxprofit = prices[i] - lowestprice

        return maxprofit

    # --------------------------------------------------------------------

    # BruteForce:  This is O(N^2) .. that's why we can do better by using DP - See Kadane's Algo ( but that doesn't submit due to reason mentioned)
    # Time Complexity O(n^2)
    def maxProfit4(self,prices):
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if maxProfit < profit:
                      maxProfit = profit
        return maxProfit

    # --------------------------------------------------------------------

    # Kadane Algorithm: (if stock price are -ve); Just in case ...
    def maxProfit_Kadane_Algo(self,prices):

        maxCur = 0 # current maximum value
        maxSoFar = 0 # maximum value found so far
        for i in range(len(prices)):
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0,maxCur) # Incase the difference falls below 0, reset it to zero.
            maxSoFar = max(maxCur,maxSoFar)
        return maxSoFar

    # when I realize the problem is to find the maximum subarray sum, it turns into using Prefix-sum to solve the problem. And what does prefix sum preSum(i) means? It means doing buy-sell operation starting from day 0 to day i. And MAX{preSum(j) - preSum(i)} is to find the day which is MOST profitable - LEAST profitable. And we need to find the day i, where the stock price is the least.

    # I spent some time convincing myself about why we need to reset to zero. By reseting maxCur to 0, essentially it means that we have found a point i where the price[i] is lower than the time we bought, and that we should then try to buy at point i to see if we can achieve a bigger gain. Because maxCur is recording the difference, the difference between price[i] and itself should be 0


    #########################################################################

    def maxProfit1(self, prices):
        if not prices:
            return 0
        # haven't sold anything can't do worse than that
        max_profit = 0
        # highest possible price
        min_buy = float('inf')
        for p in prices:
            # possible new profit = if we sell at p - what we bought at min
            max_profit = max(max_profit,p-min_buy)
            # if it is cheaper why not buy here instead and see if we can do better
            # than the current max_profit sometime later
            min_buy = min(min_buy,p)
        return max_profit

    def maxProfit2(self, prices):  # Aditya
        if not prices:
            return 0

        minPrice = prices[0]
        max_price = 0
        difference = 0
        for price in prices[1:]:
            if price < minPrice: #
                minPrice = price

            elif price > minPrice:
                difference = price - minPrice
                max_price = max(max_price,difference)
                #if difference > max_price:
                #    max_price = difference
            #print price, minPrice, difference, max_price
        return max_price

if __name__ == '__main__':

    prices1 = [7,1,5,3,6,4]
    prices2 = [3,10,7,9, 1, 5, 2]
    prices3 = [7,6,4,3,1]
    prices4 = [0, 6, -3, 7]
    s = Solution()
    #print prices
    #print "\nMax Profit: ", s.maxProfit1(prices1)
    #print "\nMax Profit: ", s.maxProfit2(prices1)
    print "\nMax Profit: ", s.maxProfit3(prices1)
    print "\nMax Profit: ", s.maxProfit4(prices1)
    print "\nMax Profit - DP: ", s.maxProfit_Kadane_Algo(prices1)



