class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxNum = float("-inf")
        res, heap = [], []
        for i in range(len(nums)): #O(n) time
            heapq.heappush(heap, [-(nums[i]), i])
            if i >= k - 1:
                while heap[0][1] < (i - k + 1):
                    popped = heapq.heappop(heap)
                    if maxNum == -(popped[0]):
                        maxNum = float("-inf")
                maxNum = max(maxNum, -heap[0][0])
                res.append(maxNum)

        return res