class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() #O(nlogn) time and O(n) space due to Python using Timsort
        res = []

        for i in range(len(nums)): #O(n) time
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k: #O(n2) time
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                
                elif total > 0:
                    k -= 1
                
                else:
                    triple = [nums[i], nums[j], nums[k]]
                    res.append(triple) #O(n2) space total because you can free choose any comination of first 2 numbers (Cant choose 3rd)
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res