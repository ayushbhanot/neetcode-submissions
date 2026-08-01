class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        for i in range(len(heights)): #O(n) time
            l, r = i - 1, i + 1
            area = heights[i]

            while l >= 0 and heights[l] >= heights[i]: #O(n2) time
                area += heights[i]
                l -= 1

            while r < len(heights) and heights[r] >= heights[i]: #O(n2) time
                area += heights[i]
                r += 1

            maxArea = max(maxArea, area)

        return maxArea