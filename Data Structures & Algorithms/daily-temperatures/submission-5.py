class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) #O(n) time and space
        stack = []

        for i in range(len(temperatures)): #O(n) time
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped

            stack.append(i)

        return res