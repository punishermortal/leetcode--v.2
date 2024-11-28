class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue_blanks = [[0, 0]]
        seen = set([(0, 0)])
        queue_blocks = []
        tmp_blocks = []
        level = 0
        directions = [
            [0, 1], 
            [0, -1], 
            [1, 0], 
            [-1, 0]
        ]
        
        while True: 
            while queue_blanks: 
                x, y = queue_blanks.pop(0)
                for dx, dy in directions: 
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen:
                        if xx == m - 1 and yy == n - 1: 
                            return level
                        if grid[xx][yy] == 0: 
                            queue_blanks.append([xx, yy])
                        else: 
                            queue_blocks.append([xx, yy])
                        seen.add((xx, yy))

            level += 1
            while queue_blocks:
                x, y = queue_blocks.pop(0)
                for dx, dy in directions: 
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen: 
                        if xx == m - 1 and yy == n - 1: 
                            return level
                        if grid[xx][yy] == 0: 
                            queue_blanks.append([xx, yy])
                        else: 
                            tmp_blocks.append([xx, yy])
                        seen.add((xx, yy))
            queue_blocks = tmp_blocks
            tmp_blocks = []
        