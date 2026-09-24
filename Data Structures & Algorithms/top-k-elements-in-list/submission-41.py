class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(n) space

        counts = []

        for key, value in countMap.items(): #O(n) time
            counts.append((value, key)) #O(n) space

        counts.sort(reverse=True) #O(nlogn) time and O(n) space due to Python's use of timsort (Built in language's default sorting algorithm)

        res = []

        for i in range(k): #O(k) time
            res.append(counts[i][1]) #O(k) space

        return res