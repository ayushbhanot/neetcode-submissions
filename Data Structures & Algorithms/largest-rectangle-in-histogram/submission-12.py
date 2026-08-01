class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        for i in range(len(heights)): #O(n) time
            area = heights[i]

            l, r = i - 1, i + 1
            while l >= 0 and heights[l] >= heights[i]: #O(n2) time
                area += heights[i]
                l -= 1

            while r < len(heights) and heights[r] >= heights[i]: #O(n2) time
                area += heights[i]
                r += 1

            maxArea = max(area, maxArea)

        return maxArea