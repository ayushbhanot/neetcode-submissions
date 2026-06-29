class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1, 1, 1, 2, 3, 3, 3] k = 2
        #[1, 3]

        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being unique
            #[1 -> 3, 2 -> 1, 3 -> 3]
        
        reverseArray = []
        for (key, value) in count.items(): #O(d) time
            reverseArray.append([value, key]) #O(d) space
        
        reverseArray.sort()
        res = []
        for i in range(len(reverseArray)-1, -1, -1):
            res.append(reverseArray[i][1])
            if len(res) == k:
                return res