class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post, res = [0] * n, [0] * n, [0] * n
        pre[0], post[n-1] = 1, 1
        #[1,2,3,4]
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * post[i]
        #O(3n) time -> O(n) time
        #O(3n) space -> O(n) space
        return res