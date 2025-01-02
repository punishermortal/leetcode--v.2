class Solution:
    def maxMoves(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for j in range(n - 1, -1, -1):
            for i in range(m):
                for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                        dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])

        return max(dp[i][0] for i in range(m))