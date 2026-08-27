class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)): #O(n) time
            array.append([nums[i], i]) #O(n) space

        array.sort() #O(nlogn) time and O(n) space (Python's timsort)

        l, r = 0, len(array) - 1

        while l < r:
            total = array[l][0] + array[r][0]

            if total == target:
                return [min(array[l][1], array[r][1]), max(array[l][1], array[r][1])]
            elif target > total:
                l += 1
            elif target < total:
                r -= 1

        return []