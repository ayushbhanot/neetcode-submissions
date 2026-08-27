class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)): #O(n) time
            for j in range(i + 1, len(nums)): #O(n2) time
                total = nums[i] + nums[j]
                if target == total:
                    return [i, j]

        return []