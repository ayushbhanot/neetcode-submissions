class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        l = 0
        for r in range(k, len(nums) + 1): #O(n) time
            maxNum = float("-inf")
            for i in range(l, r): #O(n*k) time
                maxNum = max(maxNum, nums[i]) #O(n/k) space
            res.append(maxNum)
            l += 1
        
        return res


