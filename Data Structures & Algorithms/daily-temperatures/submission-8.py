class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) #O(n) space and is it really O(1) because doesnt it take O(n) time to allocate this space??

        for i in range(len(temperatures) - 2, -1, -1): #O(n) time
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1
            if j >= len(temperatures):
                continue
            res[i] = j - i
        
        return res