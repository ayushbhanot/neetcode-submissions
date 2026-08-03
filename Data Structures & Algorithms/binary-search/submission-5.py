class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2

            if target >= nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m

        if nums[l - 1] == target:
            return l - 1
        else:
            return -1

        