class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() #O(nlogn) time and O(n) space due to Python's timsort

        for i in range(len(nums)): #O(n) time
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:    #O(n2) time
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triple = [nums[i], nums[l], nums[r]]
                    res.append(triple) #O(n2) space due to being able to pick any first 2 numbers for combination
                    r -= 1
                    while (r > l and nums[r] == nums[r + 1]):
                        r -= 1

        return res