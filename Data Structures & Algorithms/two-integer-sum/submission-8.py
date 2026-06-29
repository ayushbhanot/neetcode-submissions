class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums): #O(n) time O(1) space
            diff = target - num
            if diff in seen:
                ans = [i, seen[diff]]
                return sorted(ans) #O(nlogn) time and O(n) space
            seen[num] = i #O(n) space
            #Overall O(n) time and O(n) space
