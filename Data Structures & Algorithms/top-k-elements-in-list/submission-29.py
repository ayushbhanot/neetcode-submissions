import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u=uniquenumbers but worst case u = n) so O(n) space

        heap = []
        for key, value in countMap.items():#O(u) time
            heapq.heappush(heap, [value, key]) #O(u) space
            if len(heap) > k: 
                heapq.heappop(heap) #O(logk) time

        res = []
        for i in range(k): #O(k) time
            popped = heapq.heappop(heap)
            res.append((popped[1])) #O(k) space and O(klogu) time

        return res