class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        targetRow = -1
        leftRow, rightRow = 0, rows - 1

        while leftRow <= rightRow: #O(log(rows)) time and O(1) space
            middleRow = leftRow + (rightRow - leftRow) // 2

            if matrix[middleRow][0] <= target <= matrix[middleRow][-1]:
                targetRow = middleRow
                break
            
            elif target < matrix[middleRow][0]:
                rightRow = middleRow - 1
            elif target > matrix[middleRow][-1]:
                leftRow = middleRow + 1
        
        if targetRow == -1:
            return False

        leftCol, rightCol = 0, cols - 1

        while leftCol <= rightCol: #O(log(cols)) time and O(1) space
            middleCol = leftCol + (rightCol - leftCol) // 2
        
            if target == matrix[targetRow][middleCol]:
                return True
            
            elif target > matrix[targetRow][middleCol]:
                leftCol = middleCol + 1
            elif target < matrix[targetRow][middleCol]:
                rightCol = middleCol - 1

        return False #O(logr) + O(logc) time => O(log(r * c)) time and O(1) space total