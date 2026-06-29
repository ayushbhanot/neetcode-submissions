class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        length = 9

        for row in range(length):
            seen = set()
            for i in range(length):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(length):
            seen = set()
            for i in range(length):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for box_row in (0, 3, 6):
            for box_col in (0, 3, 6):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[row + box_row][col + box_col] == ".":
                            continue
                        if board[row + box_row][col + box_col] in seen:
                            return False
                        seen.add(board[row + box_row][col + box_col])


        return True
