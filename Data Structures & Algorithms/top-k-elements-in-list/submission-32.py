class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u = unique numbers space)

        for key, value in countMap.items(): #O(u) time
            freq[value].append(key) #O(u) space

        res = []

        for i in range(len(freq) - 1, 0, -1): #O(n) time
            for num in freq[i]: #O(u) time
                res.append(num) #O(k) space
                if len(res) == k:
                    return res
        return []