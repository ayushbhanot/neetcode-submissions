class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for i in range(len(nums)): #O(n) time 
            if nums[i] == 0:
                zeros += 1
                if zeros > 1:
                    return [0] * len(nums)
                continue
            prod *= nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                nums = [0] * len(nums)
                nums[i] = prod
                return nums
            nums[i] = int(prod/nums[i])
        return nums