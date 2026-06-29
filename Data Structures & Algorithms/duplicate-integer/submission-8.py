class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums) #Makes it easier
        nums.sort() #O(nlogn) time

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False #O(nlogn) time O(1) space