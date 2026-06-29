class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        sets = set(nums) #O(n) space and time

        counters = [1] * len(nums) #O(n) space and time
        
        for i in range(len(nums)): #O(n) time
            curr = nums[i]
            
            if curr - 1 in sets:
                continue

            while curr + 1 in sets:
                counters[i] += 1
                curr += 1
        
        return max(counters) #O(n) time
                