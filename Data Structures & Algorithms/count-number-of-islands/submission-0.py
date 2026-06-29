class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid) #Number of rows is the length of grid
        COLS = len(grid[0]) #Number of columns is the length of any indexs of grid lets pick 0

        islands = 0

        visit = set()

        def dfs(r,c, visit):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == "0"): #Out of bounds or already visited
                return 

            if (grid[r][c] == "1" and (r,c) not in visit ):
                visit.add((r,c))
                dfs(r+1,c, visit)
                dfs(r-1,c, visit)
                dfs(r,c+1, visit)
                dfs(r,c-1, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == "1" and (r,c) not in visit):
                    dfs(r,c, visit)
                    islands += 1
        return islands
            
                



