class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for num in nums:
            duplicates.add(num)
        
        if len(duplicates) != len(nums):
            return True
        return False