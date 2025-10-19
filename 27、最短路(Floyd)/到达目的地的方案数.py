class Solution:
    inf = 1e20
    mod = 1000000007

    def initEdges(self, n):
        self.f = [[] for _ in range(n)]
        self.c = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.f[i].append(0 if i == j else self.inf)
                self.c[i].append(1 if i == j else 0)
    
    def addEdge(self, u, v, w):
        if w < self.f[u][v]:
            self.f[u][v] = w
            self.c[u][v] = 1

    def FloyedWarshall(self, n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.f[i][k] == self.inf or self.f[k][j] == self.inf:
                        continue
                    
                    if i == k or j == k:
                        continue

                    if self.f[i][k] + self.f[k][j] < self.f[i][j]:
                        self.f[i][j] = self.f[i][k] + self.f[k][j]
                        self.c[i][j] = self.c[i][k] * self.c[k][j] % self.mod
                    elif self.f[i][k] + self.f[k][j] == self.f[i][j]:
                        self.c[i][j] += self.c[i][k] * self.c[k][j] % self.mod
                        if self.c[i][j] >= self.mod:
                            self.c[i][j] %= self.mod

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        self.initEdges(n)
        for r in roads:
            self.addEdge(r[0], r[1], r[2])
            self.addEdge(r[1], r[0], r[2])
        self.FloyedWarshall(n)
        return self.c[0][n-1]







