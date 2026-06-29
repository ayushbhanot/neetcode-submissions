class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums: #O(n) time
            countMap[num] = countMap.get(num, 0) + 1 #O(u=unique numbers) space

        
        res = []
        for key, value in countMap.items(): #O(u=unique numbers) time
            res.append([value, key]) #O(u) space
        
        res.sort() #O(ulogu) time

        ans = []
        for i in range(len(res) - 1, -2, -1): #O(u) time
            if len(ans) == k:
                return ans
            ans.append(res[i][1]) #O(u) space

        return []