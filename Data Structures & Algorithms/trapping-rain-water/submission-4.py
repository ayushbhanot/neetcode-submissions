class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftArray, rightArray = [0 for i in range(len(height))], [0 for i in range(len(height))]
        leftHeight, rightHeight = 0, 0
        maxArea = 0

        for i in range(len(height)): #O(n) time
            leftHeight = max(leftHeight, height[i])
            leftArray[i] = leftHeight

        for i in range(len(height) - 1, -1, -1): #O(n) time
            rightHeight = max(rightHeight, height[i])
            rightArray[i] = rightHeight

        for i in range(len(height)): #O(n) time
            containerHeight = min(leftArray[i], rightArray[i])
            area = containerHeight - height[i]

            maxArea += area

        return maxArea