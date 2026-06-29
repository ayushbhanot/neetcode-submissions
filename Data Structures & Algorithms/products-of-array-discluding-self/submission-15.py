class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product, zeroCount = 1, 0

        for i in range(len(nums)): #O(n) time
            if nums[i] == 0:
                zeroCount += 1
                continue
            product = product * nums[i]

        output = [0] * len(nums) #O(n) time & space
    
        if zeroCount > 1:
            return output

        for i in range(len(nums)): #O(n) time
            if nums[i] == 0:
                output = [0] * len(nums) #O(n) time and space
                output[i] = product
                return output
            output[i] = product // nums[i]
        
        return output
