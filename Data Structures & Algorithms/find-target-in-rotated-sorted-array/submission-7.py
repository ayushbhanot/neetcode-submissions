class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)

        l, r = 0, N - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        minIndex = r

        if nums[minIndex] <= target <= nums[N - 1]:
            l, r = minIndex, N - 1
        else:
            l, r = 0, minIndex - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return -1