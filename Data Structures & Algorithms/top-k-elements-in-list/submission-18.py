class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        for i in range(len(nums) + 1): #O(n) time
            bucket.append([]) #O(n) space

        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being number of unique elements

        for (key, value) in count.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res