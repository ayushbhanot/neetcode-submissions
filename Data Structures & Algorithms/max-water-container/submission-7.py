class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)): #O(n) time
            for j in range(i + 1, len(heights)): #O(n2) time
                width = j - i
                height = min(heights[i], heights[j])

                area = width * height

                maxArea = max(area, maxArea)

        return maxArea