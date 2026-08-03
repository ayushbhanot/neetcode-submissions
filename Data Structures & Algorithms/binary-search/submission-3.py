class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        m = (r - l) // 2

        while nums[m] != target and l <= r:
            m = l + (r - l) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            
        if nums[m] == target:
            return m
        else:
            return -1