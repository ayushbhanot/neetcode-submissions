class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)

        while l < r:

            m = l + (r - l) // 2

            if target > nums[m]:
                l = m + 1           #[0, 1, 2, 3, 4, 5]
            elif target <= nums[m]: #[1, 2, 4, 4, 4, 6]
                r = m
        
        targetIndex = r

        if 0 <= targetIndex < len(nums) and nums[targetIndex] == target:
            return targetIndex

        else:
            return -1