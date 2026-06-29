# grid = [
# [1,1,0],
# [0,1,1],
# [0,1,2]
# ]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visit = set()
        minutes = -1
        ROWS, COL = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))

            
        while len(queue) > 0:
            for i in range(len(queue)):
                (r,c) = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2

                #Insert ap;roved base case

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    if (min(dr + r, dc + c) < 0 or dr + r >= ROWS or dc + c >= COL or grid[dr+r][dc+c] == 0 or grid[dr+r][dc+c] == 2 or (r+dr,c+dc) in visit):
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,dc+c))
            minutes += 1
        if minutes == -1:
            minutes += 1
        for r in range(ROWS):
            for c in range(COL):
                if grid[r][c] == 1:
                    minutes = -1
        return minutes
        
