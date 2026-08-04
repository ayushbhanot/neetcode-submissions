class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2

            row = m // cols
            col = m % cols

            val = matrix[row][col]

            if target == val:
                return True
            elif target > val:
                l = m + 1
            elif target < val:
                r = m - 1

        return False #O(log(m*n)) time and O(1) space, Single Pass Solution