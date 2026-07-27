class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1): #O(n) time
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                tmp = j
                j += res[j]
                if j == tmp:
                    break
                    
            if temperatures[j] > temperatures[i]:
                res[i] = j - i

        return res