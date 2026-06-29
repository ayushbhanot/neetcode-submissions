class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums): #O(n) time
            seen[num] = i #O(n) space

        for i, num in enumerate(nums): #O(n) time
            diff = target - num
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]
            