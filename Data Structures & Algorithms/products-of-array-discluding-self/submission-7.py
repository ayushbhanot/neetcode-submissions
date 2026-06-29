class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #O(n) space
        for i in range(len(nums)): #O(n) time
            for j in range(len(nums)): #O(n2) time now
                if i == j:
                    continue
                res[i] *= nums[j]

        return res