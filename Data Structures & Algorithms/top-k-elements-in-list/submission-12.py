class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being number of uniqe elements
        
        array = []
        for (key, value) in count.items(): #O(d) time
            array.append([value, key]) #O(d) space

        array.sort() #O(dlogd) time

        res = []
        for i in range(len(array) - 1, -1, -1): #O(d) time
            res.append(array[i][1]) #O(d) space worst-case but average shuold be O(k)
            if len(res) == k:
                return res

        #Overall O(dlogd) time and O(d) space?? or O(n) time