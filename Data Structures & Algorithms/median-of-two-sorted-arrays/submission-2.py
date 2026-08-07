class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        maxLength = max(len(nums1), len(nums2))

        i, j = 0, 0
        nums = []

        while i < len(nums1) and j < len(nums2):
            
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
        
        r = len(nums) - 1
        if len(nums) % 2 == 0:
            return (nums[r // 2] + nums[(r // 2) + 1]) / 2
        else:
            return nums[r // 2]
            