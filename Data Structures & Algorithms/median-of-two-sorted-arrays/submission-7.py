class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = [], []

        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        totalNums = len(A) + len(B)

        leftSeg = totalNums // 2


        A_l, A_r = 0, len(A) - 1
        while True:
            A_m = A_l + (A_r - A_l) // 2

            B_m = leftSeg - (A_m + 1) - 1

            A_lval = A[A_m] if A_m >= 0 else float('-inf')
            B_lval = B[B_m] if B_m >= 0 else float('-inf')

            A_rval = A[A_m + 1] if A_m + 1 < len(A) else float('inf')
            B_rval = B[B_m + 1] if B_m + 1 < len(B) else float('inf')

            if A_lval <= B_rval and B_lval <= A_rval:
                if totalNums % 2 == 0:
                    return (max(A_lval, B_lval) + min(A_rval, B_rval)) / 2
                else:
                    return min(A_rval, B_rval)

            elif A_lval > B_rval:
                A_r = A_m - 1
            elif B_lval > A_rval:
                A_l = A_m + 1