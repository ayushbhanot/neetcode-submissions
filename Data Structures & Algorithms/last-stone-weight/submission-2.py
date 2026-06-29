class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)): #Setup for MAX Heap
            stones[i] = stones[i] * -1

        heapq.heapify(stones)


        while (len(stones) >  1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
           
            if (x > y):
                heapq.heappush(stones, -(x - y))
            if (y > x):
                heapq.heappush(stones, -(y - x))
            
        if (len(stones) == 0):
                return 0
        return -stones[0]