class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}#O(n) space
        for i, num in enumerate(nums): #O(n) time
            targetNum = target - num
            if targetNum in seen:
                return [seen[targetNum], i]
            seen[num] = i