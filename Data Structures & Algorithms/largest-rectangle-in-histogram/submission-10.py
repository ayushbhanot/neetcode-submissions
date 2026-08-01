class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        n = len(heights)
        stack = []
        leftMost = [-1] * n

        for i in range(n): #O(n) time
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]        
            stack.append(i) #O(n) space
        
        rightMost = [n] * n
        stack = []
        for i in range(n - 1, -1, -1): #O(n) time
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i) #O(n) space

        maxArea = 0
        for i in range(n): #O(n) time
            maxArea = max(maxArea, (rightMost[i] - leftMost[i] - 1) * heights[i])

        return maxArea