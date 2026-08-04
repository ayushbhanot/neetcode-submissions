class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])


        row, col = 0, cols - 1

        while row < rows and col >= 0:
            val = matrix[row][col]

            if val == target:
                return True

            elif target > val:
                row += 1
            elif target < val:
                col -= 1

        return False #Staircase approach O(m + n) time O(1) space because at max you go left times and down r times