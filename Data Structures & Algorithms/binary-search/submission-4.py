class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, target, nums)

    def binary_search(self, l, r, target, nums) -> int:
        m = l + (r - l) // 2

        if l > r:
            return -1

        elif target == nums[m]:
            return m
        elif target > nums[m]:
            return self.binary_search(m + 1, r, target, nums)
        elif target < nums[m]:
            return self.binary_search(l, m - 1, target, nums)
        