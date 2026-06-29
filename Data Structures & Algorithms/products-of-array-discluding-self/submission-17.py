class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums) 
        output = [1] * n #O(n) time and space

        prefix = 1
        for i in range(1, n): #O(n) time
            prefix *= nums[i - 1]
            output[i] *= prefix

        postfix = 1
        for i in range(n - 2, -1, -1): #O(n) time
            postfix *= nums[i + 1]
            output[i] *= postfix

        return output
