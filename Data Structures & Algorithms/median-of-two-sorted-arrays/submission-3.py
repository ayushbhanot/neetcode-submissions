class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i])

        for j in range(len(nums2)):
            nums.append(nums2[j])

        nums.sort()

        if len(nums) % 2 == 0:
            first = nums[len(nums) // 2]
            second = nums[((len(nums)) // 2) - 1]
            return (first + second) / 2

        else:
            return nums[len(nums) // 2]