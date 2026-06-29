class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums): #O(n) time
            A.append([n, i]) #O(n) space

        A.sort() #O(nlogn) time

        i, j = 0, len(A) - 1

        while i < j: #O(n) time
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            if curr < target:
                i += 1
            else:
                j -= 1

        return []