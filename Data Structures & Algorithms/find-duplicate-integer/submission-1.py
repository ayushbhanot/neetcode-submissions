class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort() #O(nlogn) time and O(n) space due to Python's timsort built in

        l, r = 0, 1

        for r in range(r, len(nums)):
            if nums[l] == nums[r]:
                return nums[l]

            l += 1

        return None