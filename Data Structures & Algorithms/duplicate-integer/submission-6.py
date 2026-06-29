class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n): #Two pointer with nested for loop O(n2) Time but O(1) memory
                if nums[j] == nums[i]:
                    return True

        return False
