class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #Onlogn time

        for i in range(len(nums) - 1): #O(n) time
            if nums[i + 1] == nums[i]:
                return True

        return False