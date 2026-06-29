class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(0)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)): #O(n2) time
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod #O(n) space
        return res