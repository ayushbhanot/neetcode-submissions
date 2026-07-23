import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res, heap = [], []
        maxNum = float("-inf")
        l = 0
        for r in range(len(nums)): #O(n) time
            heapq.heappush(heap, [-(nums[r]), r]) #O(n) space and O(n*logn) time
            if r >= k - 1:
                while heap[0][1] < l: 
                    heapq.heappop(heap)
                res.append(-heap[0][0])
                l += 1

        return res