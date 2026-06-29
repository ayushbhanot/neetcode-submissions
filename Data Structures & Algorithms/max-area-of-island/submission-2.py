class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COL = len(grid[0])
        islands = []

        def dfs(r, c, visit) -> int:
            if (r < 0 or c < 0 or r >= ROWS or c >= COL or (r,c) in visit or grid[r][c] == 0):
                return 0

            if (grid[r][c] == 1 and (r,c) not in visit):
                visit.add((r,c))
                return 1 + dfs(r+1,c,visit) + dfs(r-1,c,visit) + dfs(r,c+1,visit) + dfs(r,c-1,visit)

            else:
                return 0

        for r in range(ROWS):
            for c in range(COL):
                if (grid[r][c] == 1 and (r,c) not in visit):
                    area = dfs(r,c,visit)
                    islands.append(area)

        for i in range(len(islands)):
            islands[i] = -islands[i]
        heapq.heapify(islands)
        if not islands:
            return 0
        else:
            return -islands[0]
                    
                    
