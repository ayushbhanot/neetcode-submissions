class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        result = []

        for i, num in enumerate(nums):
            needed = target - num

            if needed in hashMap:
                return [hashMap[needed], i]
            hashMap[num] = i
        return result