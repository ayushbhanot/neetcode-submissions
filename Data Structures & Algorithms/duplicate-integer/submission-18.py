class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #[1,1,2] [1,2,3]

        seen = set()
        for num in nums: #O(n) time
            if num in seen:
                return True
            seen.add(num) #O(n) space
                
        return False
