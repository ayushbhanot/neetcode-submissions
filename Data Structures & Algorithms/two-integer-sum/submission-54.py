class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # In this solution we can use a maps O(1) look up property and track what numbers we seen as we loop over them

        seen = {}
        for i in range(len(nums)): #O(n) time
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i #O(n) space

        return []