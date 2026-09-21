class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}

        for num in nums:

            countMap[num] = countMap.get(num, 0) + 1

        counts = []
        for key, value in countMap.items():
            counts.append((value, key))

        counts.sort()

        res = []

        for i in range(len(counts) - 1, -1, -1):
            if len(res) == k:
                return res
            res.append(counts[i][1])

        return res