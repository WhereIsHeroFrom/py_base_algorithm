import os
import sys
import queue

inf = 1000000000
isShortPath = True

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

n = int(input())
m = int(input())

u, v, w = [], [], []
for i in range(m):
    x, y, z = map(int, input().split())
    u.append(x)
    v.append(y)
    w.append(z)

s, d = map(int, input().split())

edges = initEdges(n)
for i in range(m):
    addEdge(edges, u[i], v[i], w[i])
    addEdge(edges, v[i], u[i], w[i])
dist = SPFA(edges, n, s)
if dist[d] == inf:
    print("-1\n")
else:
    print(dist[d])

edges = initEdges(n)
for i in range(m):
    addEdge(edges, u[i], v[i], 1)
    addEdge(edges, v[i], u[i], 1)
dist = SPFA(edges, n, s)
if dist[d] == inf:
    print("-1\n")
else:
    print(dist[d])