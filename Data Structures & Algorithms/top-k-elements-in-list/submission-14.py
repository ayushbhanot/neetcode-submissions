import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being the number of unique elements

        heap = []
        for (key, value) in count.items(): #O(d) time
            heapq.heappush(heap, [value, key]) #O(d) worst case space O(k) space average
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(len(heap)): #O(k) time
            res.append(heap[i][1]) #O(k) space
        return res
        