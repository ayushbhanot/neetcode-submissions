class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols, boxs = [0 for i in range(9)], [0 for i in range(9)], [0 for i in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                val = int(board[row][col])

                box_id = (row // 3) * 3 + (col // 3)

                mask = 1 << val

                if (mask & rows[row]) or (mask & cols[col]) or (mask & boxs[box_id]):
                    return False

                rows[row] = rows[row] | mask
                cols[col] = cols[col] | mask
                boxs[box_id] = boxs[box_id] | mask

        return True