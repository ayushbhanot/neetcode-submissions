class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = {}
        nums.sort() #O(nlogn) time and O(n) space due to timsort
        res = []

        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1

        for i in range(len(nums)): #O(n) time
            if (nums[i] == nums[i - 1] and i > 0):
                continue
            count[nums[i]] -= 1
            for j in range(i + 1, len(nums)): #O(n2) time
                if (nums[j] == nums[j - 1] and j > i + 1):
                    continue

                count[nums[j]] -= 1
                target = -(nums[i] + nums[j])

                if (target in count and target >= nums[j] and count[target] > 0):
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                if (nums[j] == nums[j - 1] and j > i + 1):
                    continue
                count[nums[j]] += 1

        return res