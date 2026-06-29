class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(height)): #O(n) time
            while stack and height[stack[-1]] <= height[i]:
                mid = stack.pop()
                if stack:
                    right = height[i]
                    left = stack[-1]
                    width = i - left - 1
                    heights = min(right, height[left]) - height[mid]
                    maxArea += width * heights
            stack.append(i)

        return maxArea