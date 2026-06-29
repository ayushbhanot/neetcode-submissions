class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(point: List[int]) -> float:
            if (len(point) != 2):
                return
            else:
                return abs(((point[0] ** 2) + (point[1] ** 2)) ** 0.5)
        
        distanceList = []
        heapq.heapify(distanceList)
        result = []

        for point in points:
            distance = getDistance(point)
            heapq.heappush(distanceList, (distance, point))
        
        for i in range(k):
            _, pointer = heapq.heappop(distanceList)
            result.append(pointer)

        return result
