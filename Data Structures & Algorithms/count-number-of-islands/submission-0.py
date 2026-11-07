class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        def dfs(cr, cc):
            grid[cr][cc] = '0'
            for i, j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = cr + i, cc + j
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                    dfs(nr, nc)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt
        