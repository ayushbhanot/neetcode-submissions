class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        for num in nums: #O(n) time
            if num == 0:
                zeros += 1
                continue
            prod *= num
        if zeros > 1:
            return [0] * len(nums)
        for i in range(len(nums)): #O(n) time
            if nums[i] == 0:
                res = [0] * len(nums) #O(n) space
                res[i] = prod
                return res
            else:
                nums[i] = int(prod/nums[i])
        return nums
        