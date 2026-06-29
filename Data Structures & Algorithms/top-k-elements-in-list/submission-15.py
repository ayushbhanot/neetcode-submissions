class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being unique elements

        
        for (key, value) in count.items(): #O(d) time
            bucket[value].append(key) #O(d) space

        res = []
        for i in range(len(bucket) - 1, 0, -1): #O(d) time
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
