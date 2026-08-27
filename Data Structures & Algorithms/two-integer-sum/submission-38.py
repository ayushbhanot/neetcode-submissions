class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)):
            array.append([nums[i], i])
        array.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            total = array[l][0] + array[r][0]

            if total > target:
                r -= 1
            elif total < target:
                l += 1
            elif total == target:
                return [min(array[l][1], array[r][1]), max(array[l][1], array[r][1])]

        return []