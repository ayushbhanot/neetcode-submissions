class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)): #O(n) time
            for j in range(i + 1, len(heights)): #O(n2) time
                width = j - i
                height = min(heights[i], heights[j]) #O(2) time and O(1) space so O(1) both
                area = width * height

                maxArea = max(maxArea, area) #O(2) time and O(1) space so O(1) both

        return maxArea