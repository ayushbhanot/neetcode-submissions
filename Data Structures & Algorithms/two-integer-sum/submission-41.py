class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        for i in range(len(nums)): #O(n) time O(n) space
            need = target - nums[i]
            if need in have:
                return [have[need], i]
            have[nums[i]] = i
        return []