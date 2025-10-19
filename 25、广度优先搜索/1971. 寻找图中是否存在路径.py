import queue

class Solution:
    def initEdges(self, n):
        self.edges = [ [] for _ in range(n) ]
    
    def addEdge(self, u, v):
        self.edges[u].append(v)
    
    def bfs(self, n, s):
        visited = [False for _ in range(n)]
        visited[s] = True
        q = queue.Queue()
        q.put(s)

        while not q.empty():
            u = q.get()
            for v in self.edges[u]:
                if False == visited[v]:
                    visited[v] = True
                    q.put(v)
        
        return visited

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.initEdges(n)
        for e in edges:
            self.addEdge(e[0], e[1])
            self.addEdge(e[1], e[0])
        visited = self.bfs(n, source)
        return visited[destination]