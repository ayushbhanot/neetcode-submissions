class Solution:
    def trap(self, height: List[int]) -> int:
        areas = []

        maxArea = 0

        for i in range(len(height)): #O(n) time 
            l, r = 0, len(height) - 1

            leftHeight, rightHeight = 0, 0

            while l < i: #O(n2) time
                leftHeight = max(height[l], leftHeight)
                l += 1

            while r > i: #O(n2) time
                rightHeight = max(rightHeight, height[r])
                r -= 1

            containerHeight = min(rightHeight, leftHeight)

            area = containerHeight - height[i]
            if area > 0:
                maxArea += area
        
        return maxArea
