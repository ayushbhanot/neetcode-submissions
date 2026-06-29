class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    indices.add(i)
                    indices.add(j)
        result = []
        result = list(indices)
        return result