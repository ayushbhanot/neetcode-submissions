class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for num in nums:#O(n) time
            if num in duplicates: #O(1) time for lookup
                return True

            duplicates.add(num)

        return False #O(n) time and space