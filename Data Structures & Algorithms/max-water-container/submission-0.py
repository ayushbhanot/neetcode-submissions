import heapq

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heap = []

        for i in range(len(heights)): #O(n) time

            for j in range(len(heights)): #O(n2) time
                if j == i:
                    continue
                width = max(i, j) - min(i, j)
                height = min(heights[i], heights[j])
                area = width * height
                heapq.heappush(heap, -(area)) #O(n2) space and you can disregard time because even thouguh O(logn), O(n2) > O(n2logn) for time


        return -(heapq.heappop(heap))
                