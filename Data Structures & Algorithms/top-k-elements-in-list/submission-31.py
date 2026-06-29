import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u = unique numbers) space

        heap = []
        res = []
        for key, value in countMap.items(): #O(u) time
            heapq.heappush(heap, [value, key])
            if len(heap) > k: #O(k + 1) space = O(k)
                heapq.heappop(heap)

        for i in range(k): #O(k) time
            res.append(heapq.heappop(heap)[1])
        return res