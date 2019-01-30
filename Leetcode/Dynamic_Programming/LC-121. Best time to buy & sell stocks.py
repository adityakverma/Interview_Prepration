
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# -----------------------------------------------------------------------------------

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit


    # -----------------------------------------------------
    # NOTE KADANE ALGO is only good when - input are -ve AND least element is not the last element of array

    # Kadane Algorithm: (ONLY IF stock price are -ve AND least element is not last element ); #
    # However this is NOT ACCEPTED here by leetcode
    # because fails testcase when [7,6,4,3,1] . Output should be 0. This gives 6.

    # Another example [ 6, -3, -7] where expected answer is 0 but algo gives 13 which is wrong.
    # So kandane's algo is not accepted here, but its good to know if inputs are -ve 'AND' least element is
    # not the last element of array. <=== IMP NOTE

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxCur = 0  # current maximum value
        maxSoFar = 0  # maximum value found so far

        for i in range(len(prices)):
            maxCur += prices[i] - prices[i - 1]
            maxCur = max(0, maxCur)  # Incase the difference falls below 0, reset it to zero.
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

        # when I realize the problem is to find the maximum subarray sum, it turns into using Prefix-sum to solve the problem. And what does prefix sum preSum(i) means? It means doing buy-sell operation starting from day 0 to day i. And MAX{preSum(j) - preSum(i)} is to find the day which is MOST profitable - LEAST profitable. And we need to find the day i, where the stock price is the least.
        # I spent some time convincing myself about why we need to reset to zero. By reseting maxCur to 0, essentially it means that we have found a point i where the price[i] is lower than the time we bought, and that we should then try to buy at point i to see if we can achieve a bigger gain. Because maxCur is recording the difference, the difference between price[i] and itself should be 0

    # -----------------------------------------------------

