class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort() #O(nlogn) time

        res = 0

        curr, streak, i = nums[0], 0, 0
        while i < len(nums): #O(n) time
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(streak, res)

        return res