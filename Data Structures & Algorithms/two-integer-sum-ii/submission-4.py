class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)): #O(n) time
            for j in range(i + 1, len(numbers)): #O(n2) time
                if j == i:
                    continue

                total = numbers[i] + numbers[j]
                if total == target:
                    return [i + 1, j + 1]
        return []