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

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a / gcd(a, b) * b

n = 2021
edges = initEdges(n)

for i in range(1, n+1) :
    for j in range(1, i + 22) :
        if i - j > 21 :
            continue
        if j > n:
            break
        addEdge(edges, i, j, lcm(i, j))

dist = SPFA(edges, n, 1)
print( int(dist[n]) )