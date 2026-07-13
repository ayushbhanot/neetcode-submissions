class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        for i in range(len(prices)): #O(n) time
            for j in range(i + 1, len(prices)): #O(n2) time
                profit = prices[j] - prices[i]
                maxP = max(profit, maxP)

        return maxP