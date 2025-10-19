class Solution:
    inf = 1e20

    def initEdges(self, n):
        self.f = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.f[i].append(0 if i == j else self.inf)
    
    def addEdge(self, u, v, w):
        if w < self.f[u][v]:
            self.f[u][v] = w

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

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.initEdges(n)
        for t in times:
            self.addEdge( t[0]-1, t[1]-1, t[2] )
        self.FloyedWarshall(n)
        ret = max(self.f[k-1])
        if ret == self.inf:
            ret = -1
        return ret