class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1

        buckets = [[] for i in range(len(nums))]
        for key, value in numCount.items():
            buckets[value - 1].append(key)

        #[1, 2, 2, 3, 3, 3]
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    break
            if len(res) == k:
                break
        
        return res