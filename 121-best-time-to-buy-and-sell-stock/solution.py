class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        buy  = prices[0]
        profit = 0
        maxprofit = 0
        for price in prices[1:]:
            if price<buy:
                if profit > maxprofit:
                    maxprofit = profit
                profit = 0
                buy  = price
                sell = 0
            elif price>sell:
                sell = price
                profit = sell - buy
        if profit < maxprofit:
            return maxprofit
        return profit

class BadSolution(Solution):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, buy in enumerate(prices[:-1]):
            for sell in prices[i+1:]:
                if sell-buy>profit:
                    profit = sell-buy
        return profit