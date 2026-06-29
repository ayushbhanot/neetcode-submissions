class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for i in range(9): #O(1) time since its constant
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for box_row in (0, 3, 6):
            for box_col in (0, 3, 6):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + box_row][j + box_col] == ".":
                            continue
                        if board[i + box_row][j + box_col] in seen:
                            return False
                        seen.add(board[i + box_row][j + box_col])

        return True        