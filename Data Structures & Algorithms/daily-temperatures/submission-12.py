class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #O(n) space

        for i in range(len(temperatures)): #O(n) time
            for j in range(i, len(temperatures)): #O(n2) time
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break

        return res # => O(n2) time & O(n) space