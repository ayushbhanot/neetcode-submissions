class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary Search same thing to find min index in rotated array for pivot O(logn) time and O(1) space

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2 #avoids int overflow

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        pivot = r
        
        res = self.binary_search(nums, 0, r - 1, target)
        if res == -1:
            return self.binary_search(nums, r, len(nums) - 1, target)
        else:
            return res


    # Define a helper function that searches a sorted array for a target O(logn) time and O(1) space each call   
    def binary_search(self, arr: List[int], l: int, r: int, target: int) -> int:

        while l <= r:
            m = l + (r - l) // 2

            if arr[m] == target:
                return m

            elif target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
        
        return -1