class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       maxim = 0 
       min_price = prices[0]
       for i in range(1, len(prices)):
            if prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > maxim:
                    maxim = profit
            else:
                min_price = prices[i]
       return maxim