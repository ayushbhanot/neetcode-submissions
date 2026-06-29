class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space d being number of unique elements

        array = []
        for (key, value) in count.items(): #O(d) time
            array.append([value, key]) #O(d) space

        array.sort() #O(dlogd) time
        
        result = []
        for i in range(len(array) - 1, -1, -1): #O(d) time
            result.append(array[i][1])
            if len(result) == k:
                return result