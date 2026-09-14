class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: #O(n) time
            if num in seen:
                return True
            seen.add(num) #O(n) space
        
        return False