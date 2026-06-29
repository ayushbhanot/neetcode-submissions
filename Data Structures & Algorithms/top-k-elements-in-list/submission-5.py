class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = 1 + count.get(num, 0) #O(d) space as d being number of unique keys

        reverseCount = []
        for (key, value) in count.items(): #O(d) time
            reverseCount.append([value, key]) #O(d) space

        reverseCount.sort() #O(dlogd) time

        res = []
        for i in range(len(reverseCount) - 1, -1, -1): #O(k) time because of if statement or no?
            res.append(reverseCount[i][1])
            if len(res) == k:
                return res
