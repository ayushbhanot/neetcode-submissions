class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0
        for r in range(len(nums)): #O(n) time
            if r >= k - 1:
                maxNum = nums[r]
                for j in range(l, r + 1):
                    maxNum = max(maxNum, nums[j])
                res.append(maxNum)
                l += 1
            

        return res