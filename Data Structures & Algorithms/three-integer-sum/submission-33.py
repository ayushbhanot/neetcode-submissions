class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {}

        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(n) space

        nums.sort() #O(nlogn) time and O(n) space due to Python's timsort

        for i in range(len(nums)): #O(n) time
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            count[nums[i]] -= 1
            for j in range(i + 1, len(nums)): #O(n2) time
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                count[nums[j]] -= 1

                target = -(nums[i] + nums[j])

                if (target in count and count[target] > 0 and target >= nums[j]):
                    triple = [nums[i], nums[j], target]
                    res.append(triple) #O(n2) space due to being able to choose any combination of first 2 numbers

            for j in range(i + 1, len(nums)): #O(n2) time
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                count[nums[j]] += 1

        return res
