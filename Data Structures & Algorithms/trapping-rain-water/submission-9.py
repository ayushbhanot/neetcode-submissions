class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxArea = 0

        for i in range(len(height)): #O(n) time
            l, r = 0, len(height) - 1
            leftMax, rightMax = height[l], height[r]

            while l < i: #O(n2) time
                l += 1
                leftMax = max(leftMax, height[l])

            while r > i: #O(n2) time
                r -= 1
                rightMax = max(rightMax, height[r])
            
            area = min(leftMax, rightMax) - height[i]
            maxArea += area

        return maxArea