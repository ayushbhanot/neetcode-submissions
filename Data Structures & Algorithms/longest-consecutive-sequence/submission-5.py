class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        store = set(nums)
        
        for i in range(len(nums)): #O(n) time
            streak, curr = 0, nums[i]
            while curr in store:
                streak += 1
                curr += 1
            res = max(streak, res)

        return res