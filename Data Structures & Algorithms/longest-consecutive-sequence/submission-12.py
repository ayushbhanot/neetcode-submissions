class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        if not nums:
            return res

        nums.sort() #O(nlogn) time

        streak, curr = 0, nums[0]
        i = 0

        # [1, 2, 2, 3]

        while i < len(nums): #O(n) time
            if curr != nums[i]:
                curr = nums[i]
                streak = 0

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            
            curr += 1
            streak += 1
            res = max(streak, res)
            i += 1

        return res
