class Solution:
    def dfs(self, matrix, m, n, x, y):
        if self.dp.get( (x,y) ):
            return self.dp[ (x, y) ]

        ret = 1
        for d in self.dir:
            tx = x + d[0]
            ty = y + d[1]
            if tx < 0 or tx >= m or ty < 0 or ty >= n:
                continue
            if matrix[tx][ty] <= matrix[x][y]:
                continue
            
            l = self.dfs(matrix, m, n, tx, ty)
            if l + 1 > ret:
                ret = l + 1
        self.dp[ (x,y) ] = ret
        return ret

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dir = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )
        self.dp = {}

        m = len(matrix)
        n = len(matrix[0])
        ret = 1
        for i in range(m):
            for j in range(n):
                v = self.dfs(matrix, m, n, i, j)
                if v > ret:
                    ret = v
        return ret