import os
import sys
import queue
import math

inf = -1000000000
isShortPath = False

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

def initEdges(n):
    edges = [[] for i in range(n+1)]
    return edges

def addEdge(edges, u, v, w):
    edges[u].append( Edge(v, w) )

def SPFAInit(n, s):
    q = queue.Queue()
    dist = [inf for _ in range(n+1)]
    inqueue = [False for _ in range(n+1)]
    dist[s] = 0
    q.put(s)
    inqueue[s] = True
    return q, inqueue, dist

def SPFAUpdate(edges, u, q, inqueue, dist):
    for e in edges[u]:
        v = e.v
        w = e.w

        if isShortPath:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not inqueue[v]:
                    inqueue[v] = True
                    q.put(v)
        else:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                if not inqueue[v]:
                    inqueue[v] = True
                    q.put(v)

def SPFA(edges, n, s):
    q, inqueue, dist = SPFAInit(n, s)
    while not q.empty():
        u = q.get()
        inqueue[u] = False
        SPFAUpdate(edges, u, q, inqueue, dist)
    return dist

n, m, t = map(int, input().split())
edges = initEdges(n+1)
for i in range(m):
    u, v, w = input().split()
    u, v, w = int(u), int(v), float(w)
    w = math.log10(w)
    addEdge(edges, u, v, w)
    addEdge(edges, v, u, w)

dist = SPFA(edges, n, 1)
if dist[n] <= inf:
    print(-1)
else:
    ans = '%.8f' % ( math.pow(10, dist[n]) * t )
    print(ans)