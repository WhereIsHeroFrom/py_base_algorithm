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

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.initEdges(n)
        hash = {}
        for r in restricted:
            hash[r] = True
        for e in edges:
            u = e[0]
            v = e[1]
            if not hash.get(u) and not hash.get(v):
                self.addEdge(u, v)
                self.addEdge(v, u)
        visited = self.bfs(n, 0)
        ans = 0
        for v in visited:
            if v:
                ans += 1
        return ans