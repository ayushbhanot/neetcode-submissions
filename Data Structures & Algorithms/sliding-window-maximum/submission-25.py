from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        res = []
        q = deque()

        for i in range(len(nums)): #O(n) time
            
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i) #O(n) space

            if q and q[0] < (i - k + 1):
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]]) #O(n - k + 1) space

        return res