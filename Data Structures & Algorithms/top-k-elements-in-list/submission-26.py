import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u=uniquenumbers but worst case u = n) so O(n) space

        A = []
        for key, value in countMap.items():#O(u) time
            A.append([-value, key]) #O(u) space
        
        heapq.heapify(A) #O(u) time

        res = []
        for i in range(k): #O(k) time
            popped = heapq.heappop(A)
            res.append((popped[1])) #O(k) space and O(klogu) time

        return res