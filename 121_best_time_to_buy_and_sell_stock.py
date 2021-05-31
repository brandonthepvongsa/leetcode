# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = prices[0]
        max_profit = 0
        for i, num in enumerate(prices):
                potential_profit = prices[i] - min_price
                
                if potential_profit > max_profit:
                    max_profit = potential_profit
                if num < min_price:
                    min_price = num

        return max_profit