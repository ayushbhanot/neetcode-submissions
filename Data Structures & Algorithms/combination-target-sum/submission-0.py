class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, total):
            if target < total:
                return
            if i == len(nums):
                if target == sum(path):
                    res.append(path[:])
                    return
                else:
                    return
            path.append(nums[i])
            dfs(i, total + nums[i])
            path.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res

        