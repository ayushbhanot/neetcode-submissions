import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, value in hashmap.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for pair in heap:
            res.append(pair[1])

        return res