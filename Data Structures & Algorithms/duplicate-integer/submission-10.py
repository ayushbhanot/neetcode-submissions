class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n): #O(n2) time
                if nums[i] == nums[j]:
                    return True

        return False #O(n2) time O(1) space