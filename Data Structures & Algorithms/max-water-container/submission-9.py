class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        for i in range(len(heights)): #O(n) time
            
            for j in range(i + 1, len(heights)): #O(n2) time
                height = min(heights[i], heights[j])
                width = j - i
                area = height * width
                maxArea = max(maxArea, area)

        return maxArea