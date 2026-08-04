class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)): #O(row) time
            for col in range(len(matrix[0])): #O(row * col) time
                if matrix[row][col] == target:
                    return True

        return False #Brute Force Approach checking every cell, O(r * c) time and O(1) space