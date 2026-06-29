class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[:] #O(n) time & space

        for i in range(len(nums)): #O(n) time
            product = 1
            for j in range(len(nums)): #O(n2) time
                if j == i:
                    continue
                product = product * nums[j]
            res[i] = product

        return res