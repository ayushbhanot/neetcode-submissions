class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums) + 1): #O(n) time
            freq.append([]) #O(n) space

        count = {}
        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(d) space with d being the number of unique numbers

        for (key, value) in count.items(): #O(d) time
            freq[value].append(key) #O(d) space

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res