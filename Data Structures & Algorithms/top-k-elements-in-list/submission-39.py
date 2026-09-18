class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # We can use a hashmap to store count for each u = unique number and then we can convert it to a list of tuples at the end since tuples are imutable better than 2d list since counts wont change once we get them and we can loop through reversed order and get the kth frequent element

        countMap = {}

        for i in range(len(nums)): #O(n) time

            countMap[nums[i]] = countMap.get(nums[i], 0) + 1 #O(u) space

        counts = []

        for key, value in countMap.items(): #O(u) time
            counts.append((value, key)) #O(u) space

        counts.sort() #O(ulogu) time and O(u) space due to pythons timssort usage

        res = []

        for i in range(len(counts) - 1, -1, -1): #O(k) time
            if len(res) == k:
                return res

            res.append(counts[i][1]) #O(k) space

        return res