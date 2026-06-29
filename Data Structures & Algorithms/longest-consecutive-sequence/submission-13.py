class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        store = set(nums) #O(n) space and time

        for i in range(len(nums)): #O(n) time
            if nums[i] - 1 in store:
                continue
                
            curr = nums[i]
            streak = 0
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)

        return res