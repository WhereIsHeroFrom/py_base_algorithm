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

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        self.initEdges(n)
        for i in range(n):
            for j in rooms[i]:
                self.addEdge(i, j)
        visited = self.bfs(n, 0)
        for i in range(n):
            if visited[i] == False:
                return False
        return True









