class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Brute Force Approach

        for i in range(len(nums)): #O(n) time
            if nums[i] == target:
                return i
        return -1 # O(n) time and O(1) space complexity