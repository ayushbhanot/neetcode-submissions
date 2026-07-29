class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        maxArea = 0
        for i in range(len(heights)): #O(n) time
            start = i
            while stack and stack[-1][1] > heights[i]:
                popped = stack.pop()
                maxArea = max(maxArea, popped[1] * (i - popped[0]))
                start = popped[0]
            
            stack.append([start, heights[i]]) #O(n) space
            
        while stack: #O(2n) => O(n) time
            [index, height] = stack.pop()
            maxArea = max(height * (len(heights) - index), maxArea)

        return maxArea