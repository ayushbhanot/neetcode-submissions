class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #O(nlogn) time and O(n) space due to pythons timsort

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
                    res.append(triple) #O(n2) space due ot free choice of picking first 2 numbers (can be any combination no choice for 3rd)
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1

        return res