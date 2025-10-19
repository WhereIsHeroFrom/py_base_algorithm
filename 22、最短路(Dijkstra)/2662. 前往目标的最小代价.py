class Solution:
    inf = 1e20
    hash = {}

    def findPoint(self, x, y):
        if self.hash.get( (x, y) ) == None:
            self.hash[ (x, y) ] = len( self.hash.keys() )
        return self.hash[ (x, y) ]

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

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        self.initEdges(402)
        self.hash = {}
        s = self.findPoint( start[0], start[1] )
        t = self.findPoint( target[0], target[1] )
        for sr in specialRoads:
            u = self.findPoint(sr[0], sr[1])
            v = self.findPoint(sr[2], sr[3])
            w = sr[4]
            self.addEdge(u, v, w)
        
        for (x1, y1), i in self.hash.items():
            for (x2, y2), j in self.hash.items():
                self.addEdge(i, j, abs(x1-x2) + abs(y1-y2))
        
        dist = self.dijkstra( len(self.hash.keys()), s )
        return dist[t]