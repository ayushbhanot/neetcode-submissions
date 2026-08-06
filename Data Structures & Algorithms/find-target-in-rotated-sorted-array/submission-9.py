class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        l, r = 0, N - 1


        # Binary Search way to find min in rotated array so O(logn) time and O(1) space so far

        while l < r:
            m = l + (r - l) // 2 #Best formula rather than (l + r) // 2 since this avoids IntegerOverFlow error

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        
        pivot = r
        firstSegment, secondSegment = nums[0:r], nums[r:] #O(n) time and space so this is a bottleneck

        res = self.binary_search(firstSegment, target)
        if res == -1:
            res = self.binary_search(secondSegment, target)
            if res != -1:
                return pivot + res
            else:
                return res
        else:
            return res

    
    # Define Helper method that does binary search looking for a target so it is O(logn) time and O(1) space also
    def binary_search(self, arr: List[int], target: int) -> int:

        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m] == target:
                return m
            elif target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
        
        return -1