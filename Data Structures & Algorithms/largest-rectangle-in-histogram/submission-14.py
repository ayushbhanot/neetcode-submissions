class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = []
        for i in range(len(heights)): #O(n) time
            start = i
            while stack and stack[-1][1] > heights[i]:
                popped = stack.pop()
                width = i - popped[0]
                maxArea = max(maxArea, popped[1] * width)
                start = popped[0]
            stack.append([start, heights[i]]) #O(n) space

        while stack:
            popped = stack.pop()
            width = len(heights) - popped[0]
            maxArea = max(maxArea, width * popped[1])

        return maxArea