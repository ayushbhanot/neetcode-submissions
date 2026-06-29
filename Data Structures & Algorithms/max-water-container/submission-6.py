class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r: #O(n) time
            width = r - l
            height = min(heights[l], heights[r])

            area = width * height
            maxArea = max(maxArea, area)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return maxArea