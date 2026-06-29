class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i, num in enumerate(nums):
            pairs.append([num, i])
        pairs.sort()
        
        left, right = 0, len(nums) - 1

        while left < right:
            if pairs[left][0] + pairs[right][0] == target:
                return sorted([pairs[left][1], pairs[right][1]])
            elif pairs[left][0] + pairs[right][0] < target:
                left += 1
            elif pairs[left][0] + pairs[right][0] > target:
                right -= 1
            