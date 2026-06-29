class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        maxArea = 0

        for i in range(len(height)): #O(n) time
            while stack and height[i] >= height[stack[-1]]:
                floorIndex = stack.pop()
                if stack:
                    left, right = height[stack[-1]], height[i]
                    heights = min(left, right) - height[floorIndex]
                    width = i - stack[-1] - 1
                    maxArea += width * heights
            stack.append(i)
        
        return maxArea