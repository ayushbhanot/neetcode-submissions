class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Base Case:
        if not nums:
            return 0
        
        l = 0
        for r in range(1, len(nums)):
            if nums[r] == nums[l]:
                continue
            elif nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        nums[:] = nums[:l+1]
        return len(nums)