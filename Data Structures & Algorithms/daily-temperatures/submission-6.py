class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        for i in range(len(temperatures)): #O(n) time
            for j in range(i, len(temperatures)): #O(n2) time
                if temperatures[j] > temperatures[i]:
                    res.append(j - i) #O(n) space
                    break
            if len(res) == i:
                res.append(0)
        
        return res