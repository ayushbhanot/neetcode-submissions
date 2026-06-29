class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = 1, 1, [1] * len(nums) #O(n) space for output array

        for i in range(1, len(nums)): #O(n) time
            pre *= nums[i-1]
            res[i] *= pre
        
        for i in range(len(nums) - 2, -1, -1): #O(n) time
            post *= nums[i+1]
            res[i] *= post

        return res #O(n) time, O(n) space for output array O(1) space extra