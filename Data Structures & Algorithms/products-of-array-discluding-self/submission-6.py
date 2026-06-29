class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n #O(n) space for output array
        pre, post = 1, 1
        #[1,2,3,4]
        for i in range(1, n): #O(n) time
            pre *= nums[i-1]
            res[i] *= pre

        for i in range(n-2, -1, -1): #O(n) time
            post *= nums[i+1]
            res[i] *= post

        return res