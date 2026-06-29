class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        rightArray = [0 for i in range(len(prices))] #O(n) time and space
        MaxProfit = 0

        for i in range(len(prices)): #O(n) time
            for j in range(i + 1, len(prices)): #O(n2) time
                MaxProfit = max(prices[j] - prices[i], MaxProfit)

        return MaxProfit