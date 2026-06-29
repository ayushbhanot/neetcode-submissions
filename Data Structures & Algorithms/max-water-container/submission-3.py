import heapq

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heap = []

        maxArea = 0

        for i in range(len(heights)): #O(n) time

            for j in range(i + 1, len(heights)): #O(n2) time
                if j == i:
                    continue
                width =  j - i
                height = min(heights[i], heights[j])
                area = width * height
                maxArea = max(maxArea, area)


        return maxArea
                