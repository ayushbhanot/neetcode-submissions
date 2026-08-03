class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) // 2

            if nums[m] <= target:
                l = m + 1
            elif nums[m] > target:
                 r = m

        targetIndex = l - 1
        if 0 <= targetIndex < len(nums) and nums[targetIndex] == target:
            return targetIndex
        else:
            return -1
