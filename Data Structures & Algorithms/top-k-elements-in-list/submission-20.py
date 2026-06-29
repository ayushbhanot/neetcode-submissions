class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space

        valueKey = []
        for (key, value) in count.items(): #O(d) time
            valueKey.append([value, key]) #O(d) space

        valueKey.sort() #O(dlogd) time

        res = []
        for i in range(len(valueKey) - 1, -1, -1): #O(d) time
            res.append(valueKey[i][1])
            if len(res) == k:
                return res
