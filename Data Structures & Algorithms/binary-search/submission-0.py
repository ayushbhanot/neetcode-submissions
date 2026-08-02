class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
 
        m = (r - l) // 2

        while nums[m] != target and l < r:


            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            
            m = l + (r - l) // 2
        
        if nums[m] == target:
            return m
        else:
            return -1