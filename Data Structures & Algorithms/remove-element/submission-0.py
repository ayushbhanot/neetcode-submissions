# nums = 1,1,2,3,4 val = 1

# output = 2,3,4 REMOVE ALL INSTANCES OF VAL


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l = 0

        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l