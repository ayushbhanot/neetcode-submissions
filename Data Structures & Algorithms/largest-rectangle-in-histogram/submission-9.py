class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []
        maxArea = 0

        for i in range(len(heights)): #O(n) time
            start = i
            while stack and stack[-1][1] > heights[i]:
                popped = stack.pop()
                maxArea = max(maxArea, (i - popped[0]) * popped[1])
                start = popped[0]

            stack.append([start, heights[i]]) #O(n) space

        while stack:
            popped = stack.pop()
            maxArea = max(maxArea, (len(heights) - popped[0]) * popped[1])
        
        return maxArea