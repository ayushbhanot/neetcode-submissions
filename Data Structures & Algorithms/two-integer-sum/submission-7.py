class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #O(n) time
            for j in range(i+1, len(nums)): #O(n) time
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans #O(n2) time and O(1) space