class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        for r in range(len(nums)): #O(n) time
            if r >= k - 1:
                maxNum = float("-inf")
                for j in range(l, r + 1): #O(n * k - k + 1) time
                    maxNum = max(nums[j], maxNum)
                res.append(maxNum) #O(n - k + 1) space for output aray
                l += 1

        return res #Worst case is O(n * k) time and O(n) space for output