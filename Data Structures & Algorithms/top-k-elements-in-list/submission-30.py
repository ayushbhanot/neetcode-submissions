class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u = unique numbers) space

        arr = []
        for key, value in countMap.items(): #O(u) time
            arr.append([value, key]) #O(u) space

        arr.sort() #O(ulogu) time

        res = []
        for i in range(k): #O(k) time
            res.append(arr.pop()[1]) #O(k) space
        return res