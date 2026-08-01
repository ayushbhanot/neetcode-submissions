class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0

        for i in range(len(heights)): #O(n) time
            index = i
            while stack and heights[i] < stack[-1][1]:
                [index, height] = stack.pop()
                maxArea = max((i - index) * height, maxArea)
            stack.append([index, heights[i]])

        while stack:
            [index, height] = stack.pop()
            maxArea = max(maxArea, (len(heights) - index) * height)
        return maxArea