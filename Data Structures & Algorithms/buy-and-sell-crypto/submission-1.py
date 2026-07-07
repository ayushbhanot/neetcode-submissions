class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        for i in range(len(prices)): #O(n) time
            initial = prices[i]
            for j in range(i + 1, len(prices)):
                profit = prices[j] - initial
                maxProfit = max(maxProfit, profit)

        return maxProfit