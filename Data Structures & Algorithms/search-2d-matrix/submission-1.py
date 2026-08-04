class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        leftRow, rightRow = 0, len(matrix) - 1
        targetRow = -1


        while leftRow <= rightRow:
            middleRow = leftRow + (rightRow - leftRow) // 2

            firstNumber, lastNumber = matrix[middleRow][0], matrix[middleRow][len(matrix[middleRow]) - 1]

            if firstNumber <= target <= lastNumber:
                targetRow = middleRow
                break
            elif target > lastNumber:
                leftRow = middleRow + 1
            elif target < firstNumber:
                rightRow = middleRow - 1

        if targetRow == -1:
            return False

        l, r = 0, len(matrix[targetRow]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == matrix[targetRow][m]:
                return True
            elif target < matrix[targetRow][m]:
                r = m - 1
            elif target > matrix[targetRow][m]:
                l = m + 1
        return False

        