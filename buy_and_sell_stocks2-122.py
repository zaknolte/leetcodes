from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def make_trade(buy, sell):
            if sell > buy:
                return sell - buy
            return 0

        current_buy = prices[0]
        current_sell = 0
        total_profit = 0

        for price in prices:
            if price < current_buy:
                total_profit += make_trade(current_buy, current_sell)
                current_buy = price
                current_sell = 0

            elif price > current_sell:
                current_sell = price

            elif current_sell > price:
                total_profit += make_trade(current_buy, current_sell)
                current_buy = price
                current_sell = 0

        if current_sell > current_buy:
            total_profit += make_trade(current_buy, current_sell)

        return total_profit
