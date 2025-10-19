import os
import sys

##############################################################################
#################################Dijkstra Heap################################

import heapq

inf = 100000000001

class Dist :
    def __init__(self, v, w):
        self.v = v
        self.w = w
    
    def __lt__(self, other):
        return self.w < other.w

def initEdges(n):
    return [ [] for _ in range(n) ]

def addEdge(edges, u, v, w):
    edges[u].append( Dist(v, w) )

def dijkstraInit(n, st, heap, visited, d):
    for i in range(0, n):
        d[i] = inf
        visited[i] = False
    d[st] = 0
    heapq.heappush( heap, Dist(st, d[st] ) )

def dijkstraFindMin(heap):
    return heapq.heappop(heap).v

def dijkstraUpdate(u, edges, heap, visited, d):
    if visited[u]:
        return 
    visited[u] = True
    for edge in edges[u]:
        v = edge.v
        w = edge.w
        if d[u] + w < d[v]:
            d[v] = d[u] + w
            heapq.heappush( heap, Dist(v, d[v]) )

def DijkstraHeap(n, st, edges):
    heap = []
    visited = [False for _ in range(n)]
    d = [0 for _ in range(n)]
    dijkstraInit(n, st, heap, visited, d)
    while len(heap) > 0:
        u = dijkstraFindMin(heap)
        dijkstraUpdate(u, edges, heap, visited, d)
    return d

##############################################################################


n, m = map(int, input().split())
edges = initEdges(n)
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    addEdge(edges, u, v, w)

d = DijkstraHeap(n, 0, edges)
ans = d[n-1]
if ans == inf:
    ans = -1
print(ans)