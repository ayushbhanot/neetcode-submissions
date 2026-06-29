class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue

                box_id = (row // 3) * 3 + (col // 3)

                if val in rows[row] or val in cols[col] or val in boxs[box_id]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxs[box_id].add(val)

        return True