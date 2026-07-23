import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap, res = [], []
        for i in range(len(nums)): #O(n) time
            
            heapq.heappush(heap, [-(nums[i]), i]) #O(nlogn) time and O(n) space

            if i >= k - 1:

                while heap[0][1] < (i - k + 1):
                    heapq.heappop(heap)
                
                res.append(-(heap[0][0]))

        return res #O(n) space for output