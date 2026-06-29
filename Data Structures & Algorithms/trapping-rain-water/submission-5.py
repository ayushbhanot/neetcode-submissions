class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftArray, rightArray = [0 for i in range(len(height))], [0 for i in range(len(height))]
        leftHeight, rightHeight = 0, 0
        maxArea = 0

        for i in range(len(height)): #O(n) time
            leftArray[i] = leftHeight
            leftHeight = max(leftHeight, height[i])

        for i in range(len(height) - 1, -1, -1): #O(n) time
            rightArray[i] = rightHeight
            rightHeight = max(rightHeight, height[i])

        for i in range(len(height)): #O(n) time
            containerHeight = min(leftArray[i], rightArray[i])
            area = containerHeight - height[i]
            
            if area > 0:
                maxArea += area

        return maxArea