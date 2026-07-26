class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)): #O(n) time
            for j in range(i + 1, len(temperatures)): #O(n2) time
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
            if len(res) - 1 < i:
                res.append(0) #O(n) space
        
        return res  # => O(n2) time and O(n) space