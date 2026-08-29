class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]

        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        for num, count in numCount.items():
            buckets[count - 1].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    break
                res.append(buckets[i][j])
        return res
