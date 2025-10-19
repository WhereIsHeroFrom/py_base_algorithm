class Solution:
    inf = 1e20

    def initEdges(self, n):
        self.graph = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(self.inf)
            self.graph.append(row)
    
    def addEdge(self, u, v, w):
        if w < self.graph[u][v]:
            self.graph[u][v] = w
    
    def dijkstra(self, n, s):
        dist = [self.inf for i in range(n)]
        visited = [False for i in range(n)]

        dist[s] = 0

        while True:
            minDist = self.inf
            minIndex = 0
            for i in range(n):
                if visited[i]:
                    continue
                if dist[i] < minDist:
                    minDist = dist[i]
                    minIndex = i
            if minDist == self.inf:
                break
            visited[minIndex] = True

            for i in range(n):
                if visited[i]:
                    continue
                dis = self.graph[minIndex][i]
                if dis == self.inf:
                    continue
                if dist[minIndex] + dis < dist[i]:
                    dist[i] = dist[minIndex] + dis
        return dist

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.initEdges(n)
        for e in edges:
            u = e[0]
            v = e[1]
            w = e[2]
            self.addEdge(u, v, w)
            self.addEdge(v, u, w)
        
        retCnt = 100000
        retIdx = -1
        for i in range(n-1, -1, -1):
            dist = self.dijkstra(n, i)
            cnt = 0
            for j in range(n):
                if dist[j] <= distanceThreshold:
                    cnt += 1
            if cnt < retCnt:
                retCnt = cnt
                retIdx = i
                
        return retIdx