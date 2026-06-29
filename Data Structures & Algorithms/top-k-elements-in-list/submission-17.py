import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being number of unique elements

        heap = []

        for (key, value) in count.items(): #O(d) time 
            heapq.heappush(heap, [value, key]) #O(logd) time O(d) space
            if len(heap) > k:
                heapq.heappop(heap) #O(logd)
        res = []
        for i in range(len(heap)): 
            res.append(heap[i][1])

        return res