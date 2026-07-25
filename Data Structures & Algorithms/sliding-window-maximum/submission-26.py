class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            maxNum = float("-inf")
            if i >= k - 1:
                for j in range(i - k + 1, i + 1):
                    maxNum = max(maxNum, nums[j])
                res.append(maxNum)

        return res
