class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for i in range(len(nums)): #O(n) time
            if i >= k - 1:
                maxNum = float("-inf")
                for j in range(i - k + 1, i + 1): #O(n * k) time
                    maxNum = max(maxNum, nums[j])
                res.append(maxNum) #O(n) space

        return res