class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2

            if target >= nums[m]: #Upper bound approach
                l = m + 1
            elif target < nums[m]:
                r = m

        targetIndex = l - 1
        if 0 <= targetIndex < len(nums) and nums[targetIndex] == target:
            return targetIndex
        else:
            return -1 #O(logn) time and O(1) space