import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res, heap = [], []
        for i in range(len(nums)): #O(n) time
            heapq.heappush(heap, [-(nums[i]), i]) #O(k) space

            while heap[0][1] < (i - k + 1):
                heapq.heappop(heap)
            
            if i >= k - 1:
                res.append(-(heap[0][0])) #O(n) space

        return res


            