class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
            hMap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hMap and hMap[diff] != i:
                return [min(hMap[diff], i), max(hMap[diff], i)]
        return []