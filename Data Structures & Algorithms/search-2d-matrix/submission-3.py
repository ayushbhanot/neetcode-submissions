class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)): #O(rows) time
            for col in range(len(matrix[row])): #O(rows *cols) time
                if matrix[row][col] == target:
                    return True
        return False