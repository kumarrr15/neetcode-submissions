class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        mini = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= mini:
                mini = prices[i]
            maxP = max(maxP, prices[i] - mini)
        return maxP
    
        