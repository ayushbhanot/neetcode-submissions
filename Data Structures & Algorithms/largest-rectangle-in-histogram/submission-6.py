class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0

        for i in range(len(heights)):

            start = i

            while stack and stack[-1][1] > heights[i]:
                popped = stack.pop()
                area = (i - popped[0]) * popped[1]
                maxArea = max(area, maxArea)
                start = popped[0]

            stack.append([start, heights[i]])

        while stack:
            popped = stack.pop()
            area = (len(heights) - popped[0]) * popped[1]
            maxArea = max(maxArea, area)

        return maxArea