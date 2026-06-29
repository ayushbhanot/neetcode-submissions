class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1, 1, 1, 2, 2, 3] k = 3   [1, 2, 3]

        #Key-Val pairs
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space as d is number of unique elements
        
        reverseArray = []
        #From key-value to value-key pairs
        for (key, value) in count.items(): #O(d) time
            reverseArray.append([value, key]) #O(d) space

        res = []
        reverseArray.sort() #O(nlogn) time
        for i in range(len(reverseArray) - 1, -1, -1): #O(d) time
            res.append(reverseArray[i][1]) #O(d) space
            if len(res) == k:
                return res