# grid = [
# [0,1,0],
# [1,0,0],
# [1,1,0]
# ]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        visit = set()
        ROWS, COL = len(grid), len(grid[0])
        length = 1
        queue.append((0,0))
        visit.add((0,0))

        if (grid[0][0] == 0):
            while len(queue) > 0: #While queue has values

                for i in range(len(queue)): #Loop through each value in queue to traverse level by level
                    (r,c) = queue.popleft()

                    if (r == ROWS - 1 and c == COL - 1):
                        return length #Base case hit lower right corner return path length

                    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
                    for (dr, dc) in directions:
                        if (min(dc + c, dr + r) < 0 or c + dc >= COL or r + dr >= ROWS or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit):
                            continue
                        
                        queue.append((dr + r, dc + c))
                        visit.add((dr + r, dc + c))
                length += 1
            else:
                return -1

        else:
            return -1

            
    