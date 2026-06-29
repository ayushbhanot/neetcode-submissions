class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r: #O(n) time

            total = numbers[r] + numbers[l]

            if target > total:
                l += 1
            
            if target < total:
                r -= 1

            if total == target:
                return [l + 1, r + 1]

        return [] #O(1) space