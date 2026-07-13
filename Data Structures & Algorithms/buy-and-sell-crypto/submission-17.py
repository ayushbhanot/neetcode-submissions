class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        lowestSeen = prices[0]

        for i in range(1, len(prices)): #O(n) time
            if prices[i] > lowestSeen:
                profit = prices[i] - lowestSeen
                maxP = max(profit, maxP)
            else:
                lowestSeen = prices[i]
        return maxP
