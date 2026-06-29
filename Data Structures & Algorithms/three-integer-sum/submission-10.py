class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {}
        nums.sort() #O(nlogn) time and O(n) space

        for num in nums: #O(n) time
            count[num] = count.get(num, 0) + 1 #O(n) space O(1) ammortized time

        for i in range(len(nums)): #O(n) time
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)): #O(n2) time
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                count[nums[j]] -= 1
                target = -(nums[i] + nums[j])
                
                if target in count and count[target] > 0 and target >= nums[j]:
                    triple = [nums[i], nums[j], target]
                    res.append(triple) #O(n2) space and O(1) ammortized time

            for j in range(i + 1, len(nums)): #O(n) time
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                count[nums[j]] += 1
                

        return res

        