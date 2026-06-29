class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ansLength = len(nums)*2

        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
