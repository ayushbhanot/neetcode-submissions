import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being number of unique nums

        heap = []
        for (key, value) in count.items(): #O(d) time
            heapq.heappush(heap, (value, key)) #O(d) space
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(len(heap)): #O(d) tiem even though it shuold be size k??
            result.append(heapq.heappop(heap)[1])

        return result