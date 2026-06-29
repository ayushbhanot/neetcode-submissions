class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[:] #O(n) space
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                prod *= nums[j]
            res[i] = prod #O(n2) time

        return res