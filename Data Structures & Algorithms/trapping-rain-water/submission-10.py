class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxArea = 0
        leftArray, rightArray = [0 for i in range(len(height))], [0 for i in range(len(height))] #O(2n) => O(n) time and space for both
        leftMax, rightMax = 0, 0

        for i in range(len(height)): #O(n) time
            leftArray[i] = leftMax
            leftMax = max(height[i], leftMax)

        for i in range(len(height) - 1, -1, -1): #O(n) time
            rightArray[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        for i in range(len(height)): #O(n) time
            heights = min(leftArray[i], rightArray[i])
            area = heights - height[i]
            if area > 0:
                maxArea += area
                
        return maxArea