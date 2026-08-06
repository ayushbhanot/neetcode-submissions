class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        pivot = r

        if nums[pivot] <= target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:

            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1 #Here we only binary search the segment that we KNOW the target is in rather than at random so same worst case but total case is less O(logn) time and O(1) space