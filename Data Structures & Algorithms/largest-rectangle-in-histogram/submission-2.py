class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        rectangles = float("-inf")

        for i in range(len(heights)): #O(n) time
            width = 1
            l = i - 1
            while l >= 0: #O(n2) time
                if heights[l] >= heights[i]:
                    width += 1
                else:
                    break
                l -= 1

            r = i + 1
            while r < len(heights): #O(n2) time
                if heights[r] >= heights[i]:
                    width += 1
                else:
                    break
                r += 1
            rectangles = max(rectangles, width * heights[i])
        
        return rectangles #O(n2) time and O(1) space