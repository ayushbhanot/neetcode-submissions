class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)): #O(n) time
            array.append((nums[i], i)) #O(n) space

        array.sort() #O(nlogn) time O(n) space

        i, j = 0, len(nums) - 1
        while i < j:
            total = array[i][0] + array[j][0]

            if total > target:
                j -= 1
            elif total < target:
                i += 1
            elif total == target:
                return [min(array[i][1], array[j][1]), max(array[i][1], array[j][1])]

        return []