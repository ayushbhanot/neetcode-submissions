class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        for i in range(len(heights)): #O(n) time
            start = i
            while stack and heights[i] < stack[-1][1]:
                [index, height] = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append([start, heights[i]]) #O(n) space
        
        while stack: #O(2n) => O(n) time
            [index, height] = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea