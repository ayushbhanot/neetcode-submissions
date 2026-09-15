class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute Force approach (Checking every combination)

        for i in range(len(nums)): #O(n) time
            for j in range(i + 1, len(nums)): #O(n2) time
                total = nums[i] + nums[j]
                if total == target:
                    return [i, j]

        return []