class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #O(nlogn) time and O(n) space due to Python's timsort sorting algorithm usage

        l = 0
        for r in range(1, len(nums)): #O(n) time
            if nums[r] == nums[l]:
                return True
            l += 1
        return False #O(1) space