class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low, high = 1, len(nums) - 1

        while low < high: #O(logn) time
            mid = low + (high - low) // 2

            totalNums = 0
            for i in range(len(nums)): #O(n) time
                if nums[i] <= mid:
                    totalNums += 1

            if totalNums > mid:
                high = mid
            elif totalNums <= mid:
                low = mid + 1

        return high #O(nlogn) time and O(1) space