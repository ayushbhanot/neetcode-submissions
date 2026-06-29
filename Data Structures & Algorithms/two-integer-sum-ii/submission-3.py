class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(numbers)): #O(n) time
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff], i + 1]
            seen[numbers[i]] = i + 1 #O(n) space

        return [] 