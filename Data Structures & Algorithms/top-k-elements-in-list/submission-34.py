class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1

        res = []
        for key, value in numCount.items():
            res.append((value, key))
        res.sort()
        result = []
        for i in range(len(res) - 1, -1, -1):
            result.append(res[i][1])
            if len(result) == k:
                break

        return result