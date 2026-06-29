class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k

        for i in range(len(self.nums)):
            self.nums[i] = -self.nums[i]

        heapq.heapify(self.nums)
        
        for i in range(self.k):
            result = -heapq.heappop(self.nums)

        return result