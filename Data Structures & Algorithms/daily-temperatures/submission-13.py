class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)): #O(n) time
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
            stack.append(i) #O(n) space auxillary

        return res # => O(n) time & space