
# Array, Greedy, Bloomberg

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/172025/Kadane's-Algorithm-is-still-applicable-to-this-problem-(just-one-line-changed-)
# Inspired Best Time to Buy and Sell Stock, the logic to solve this problem is same as max subarray problem.
# Compared with the original stock problem, you just need to change this line
# curSum = max(0, curSum+prices[i]-prices[i-1]) into
# curSum = max(curSum, curSum+prices[i]-prices[i-1])


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxprofit = 0

        for i in range(len(prices) - 1):
            if prices[i] <= prices[i + 1]:
                profit = prices[i + 1] - prices[i]
                maxprofit += profit
        return maxprofit



    # Using Kadane's DP algorithm
    # http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/
    # # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/172025/Kadane's-Algorithm-is-still-applicable-to-this-problem-(just-one-line-changed-)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        curSum = maxSum = 0

        for i in range(1, len(prices)):
            curSum = max(curSum, curSum + prices[i] - prices[i - 1])
            maxSum = max(maxSum, curSum)

        return maxSum


if __name__ == '__main__':

    prices1 = [7,1,5,3,6,4]

    s = Solution()
    print "\nMax Profit: ", s.maxProfit(prices1)

