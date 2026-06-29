class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftArray = [0 for i in range(len(height))] #O(n) time and space
        rightArray = [0 for i in range(len(height))] #O(n) time and space

        maxArea = 0
        leftHeight, rightHeight = 0, 0

        for i in range(len(height)): #O(n) time
            leftHeight = max(leftHeight, height[i])
            leftArray[i] = leftHeight

        for i in range(len(height) - 1 , -1, -1): #O(n) time
            rightHeight = max(rightHeight, height[i])
            rightArray[i] = rightHeight

        for i in range(len(height)): #O(n) time
            containerHeight = min(leftArray[i], rightArray[i]) #This line doesn't take O(n) time right?
            area = containerHeight - height[i]

            if area > 0:
                maxArea += area

        return maxArea