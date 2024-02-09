from typing import List
def maxProfit(prices: List[int]) -> int:
    current_min = prices[0]
    current_max = 0
    current_profit = 0
    for price in prices:
        if price < current_min:
            current_min = price
            current_max = 0
        elif price > current_max:
            current_max = price
        if current_max - current_min > current_profit:
            current_profit = current_max - current_min
            
    return current_profit
            
            
print(maxProfit(prices = [7,1,5,3,6,4]))